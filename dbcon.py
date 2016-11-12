import sqlite3
import config
import os
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
        self._is_db_exists()  # in case db file isn't exists

    def _is_db_exists(self):

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

    def _check_user_exists(self, UserObj):
        
        '''
        Check if user already exists
        if not then create one
        '''
        import pdb; pdb.set_trace();

        sql = ("SELECT COUNT(*) "
               "FROM 'users' "
               "WHERE 'telegram_id' = ?")
        
        cur = self.conn.cursor()
        cur.execute(sql, (UserObj.id,))

        self.conn.commit()

    def add_website(self, domain_name, UserObj):

        '''
        domain_name: message.text
        UserObj: message.from_user
        '''
        
        # check either user already exists
        self._check_user_exists(UserObj)

        insert_time = time.time()
        lastup = insert_time

        sql = ("INSERT INTO "
               "'websites' ('domain_name', 'lastup', 'is_down', 'insert_time') "
               "values (?, ?, 0, ?)")

        # lastup = insert_time (for the first time)
        data = (domain_name, lastup, insert_time)

        cur = self.conn.cursor()
        cur.execute(sql, data)

        # commit the changes
        self.conn.commit()
