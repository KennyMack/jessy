from core.environ import environ
import sqlite3
import os


class Connection(object):
    def __init__(self, settings):
        self.settings = settings

    def connect(self):
        self.db = sqlite3.connect(self.get_path_db())


    def get_path_db(self):
        db = "{0}/{1}".format(environ.get_env('JESSY_NAME'),
                              self.settings.DATABASE['NAME'])
        return os.path.join(self.settings.BASE_DIR, db)


    def commit(self):
        if self.db:
            self.db.commit()


    def rollback(self):
        if self.db:
            self.db.rollback()


    def close(self):
        if self.db:
            self.db.close()







"""



c = conn.cursor()

# Create table
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# We can also close the db if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

conn = sqlite3.connect('example.db')
"""
