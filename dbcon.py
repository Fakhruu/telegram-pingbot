import sqlite3
import config
import os
import json
import time
from exception import TelegramBotException  # custom exception


class SQL:

    #############################
    # Internal SQL class methods
    #############################

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


    ##################################
    # Helper functions is below here
    ##################################

    def select_where(self, getcol, table, colcomp, colval):

        sql = ("""
               SELECT %s
               FROM %s
               WHERE %s = ?
               """) % (getcol, table, colcomp)

        cur = self.conn.cursor()
        data = cur.execute(sql, (colval,)).fetchall()
        self.conn.commit()

        return data

    def update_where(self, table, setcol, setval, colcomp, colval):

        sql = ("""
               UPDATE %s
               SET %s = ?
               WHERE %s = ?
               """) % (table, setcol, colcomp)

        cur = self.conn.cursor()
        cur.execute(sql, (setval, colval, ))
        self.conn.commit()

    #############################################
    # Class main methods to be called from callers
    #############################################

    def add_user(self, UserObj):

        # check existing user if exists
        userid = self.select_where("telegram_id", "users", "telegram_id", UserObj.id)

        # if not already exists
        # then add new one
        if not userid:

            sql = ("""
                   INSERT INTO
                   users ('telegram_id', 'telegram_name', 'insert_time')
                   values (?, ?, ?)
                   """)

            cur = self.conn.cursor()
            cur.execute(sql, (UserObj.id, UserObj.first_name, time.time(), ))
            self.conn.commit()

    def add_website(self, domain_name, UserObj):

        '''
        domain_name: message.text
        UserObj: message.from_user
        '''

        # add user info to `users` table
        self.add_user(UserObj)

        # get id if exists
        webid = self.select_where('id', 'websites',
                                  'domain_name', domain_name)

        # check if this web already exists in DB
        if not webid:

            insert_time = time.time()
            lastup = insert_time

            sql = ("""
                   INSERT INTO
                   'websites' ('domain_name', 'lastup', 'is_down', 'insert_time')
                   values (?, ?, 0, ?)
                   """)

            # lastup = insert_time (for the first time)
            data = (domain_name, lastup, insert_time)

            cur = self.conn.cursor()
            webid = cur.execute(sql, data).lastrowid
            self.conn.commit()  # commit the changes

        else:
            # just take from existing website inside DB
            webid = webid[0][0]

        registered_status = self.select_where('id', 'users_websites',
                                              UserObj.id, webid)

        # if user currently don't have this website in his list
        # then add it on requests
        if not registered_status:

            sql = ("""
                   INSERT INTO
                   'users_websites' ('websites_id', 'telegram_id', 'insert_time')
                   values (?, ?, ?)
                   """)

            cur = self.conn.cursor()
            cur.execute(sql, (webid, UserObj.id, time.time(), ))
            self.conn.commit()

        else:
            raise TelegramBotException("You already added this website onto your list!")
