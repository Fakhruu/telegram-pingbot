import sqlite3
import config
import os
import sys

dbfile = config.ConfigSectionMap('CONFIG')['db']

check_dbfile = os.path.isfile(dbfile)

# connect to sql dbfile (if exist or not it is fine)
conn = sqlite3.connect(dbfile)

# if file not yet exist before
if not check_dbfile:

    ##################################
    # error checking if
    # the structure.sql isn't exist
    # then exit the program
    ##################################

    # if file don't exist
    if not os.path.isfile('./structure.sql'):
        print("Error: `structure.sql` don't exist! Exiting...")
        sys.exit(1)

    with open('./structure.sql', 'r') as f:
        if f:
            # read then execute sql syntaxes (create new db)
            sql = f.read()
            conn.executescript(sql)


def add_web(dict_data):

    '''
    dict_data: Dictionary containing data of :-
    '''

    pass
