import sqlite3
import config
import os
import json
import time
import exception  # custom exception


class SQL:

    def __init__(self):

        # get the filename for both SQL's structure and dbfile
        self.dbfile = config.ConfigSectionMap('CONFIG')['db']
        self.sqlfile = config.ConfigSectionMap('CONFIG')['sqlfile']

        # check beforehand connecting to dbfile
        self.check_dbfile = os.path.isfile(self.dbfile)

        self.conn = sqlite3.connect(self.dbfile)
        self.__is_dbfile_exists()  # in case db file isn't exists

    def __is_dbfile_exists(self):

        '''
        Check if db blob exists
        if not exists, then create one
        '''

        # if file not yet exist before
        if not self.check_dbfile:

            # if file don't exist
            if not os.path.isfile(self.sqlfile):
                raise exception.FileNotFoundError("%s don't exist!" % self.sqlfile)

            with open(self.sqlfile, 'r') as f:
                if f:
                    # read then execute SQL syntax (create new db)
                    sql = f.read()
                    self.conn.executescript(sql)

    def __check_user_exists(self, UserObj):
        
        '''
        Check if user already exists
        if not then create one
        '''

        sql = ("SELECT COUNT(*) "
               "FROM 'users' " 
               "WHERE 'telegram_id' = ?")

        cur = self.conn.cursor()
        data = cur.execute(sql, (UserObj.id,)).fetchall()

        if data[0][0] == 0:

            sql = ("INSERT INTO "
                   "'users' ('telegram_id', 'telegram_name', 'insert_time', 'web_id') "
                   "values (?, ?, ?, ?)")

            cur = self.conn.cursor()
            cur.execute(sql, (UserObj.id, UserObj.first_name, time.time(), '[]'))
            self.conn.commit()

    def get_data_table_where(self, getcol, table, colcomp, colval):

        sql = ("SELECT %s "
               "FROM '%s' "
               "WHERE '%s' = '%s'") % (getcol, table, colcomp, colval)
        
        cur = self.conn.cursor()
        data = cur.execute(sql).fetchall()
        self.conn.commit()

        return data

    def update_where(self, table, setcol, setval, colcomp, colval):

        sql = ("UPDATE '%s' "
               "SET '%s' = '%s' "
               "WHERE %s = '%s'") % (table, setcol, setval, colcomp, colval)

        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()


    def add_website(self, domain_name, UserObj):

        '''
        domain_name: message.text
        UserObj: message.from_user
        '''

        # check either user already exists
        self.__check_user_exists(UserObj)

        # apply to user
        curr_user_webid = self.get_data_table_where('web_id', 'users',
                                                    'telegram_id', UserObj.id)

        # check if this web already exists in DB
        webid = self.get_data_table_where('id', 'websites',
                                          'domain_name', domain_name)

        if not webid:

            insert_time = time.time()
            lastup = insert_time

            sql = ("INSERT INTO "
                   "'websites' ('domain_name', 'lastup', 'is_down', 'insert_time') "
                   "values (?, ?, 0, ?)")

            # lastup = insert_time (for the first time)
            data = (domain_name, lastup, insert_time)

            cur = self.conn.cursor()
            webid = cur.execute(sql, data).lastrowid
            self.conn.commit()  # commit the changes

        curr_user_webid.append(webid)

        self.update_where('users', 'web_id', json.dumps(curr_user_webid),
                          'telegram_id', UserObj.id)
