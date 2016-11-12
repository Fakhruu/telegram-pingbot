import sqlite3
import config

dbfile = config.ConfigSectionMap('CONFIG')['db']
conn = sqlite3.connect(dbfile)

def create_db():


def add_web(str):
    pass
