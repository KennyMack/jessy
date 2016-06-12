#!/usr/bin/python3
from core.environ import environ
from core.database.sqlite3.Connection import Connection
from core.database.sqlite3.Command import Command
from core.database.sql.conditions import Condition, Operation
from core.database.sql import sql_text
from importlib.machinery import SourceFileLoader
import json
import os


class Application(object):
    def __init__(self, path):
        with open(path) as data_file:

            data = json.load(data_file)

            if data.get('name'):
                self.name = data.get('name')
                environ.set_env('JESSY_NAME', self.name)

            if data.get('version'):
                self.version = data.get('version')
                environ.set_env('JESSY_VERSION', self.version)

            if data.get('author'):
                self.author = data.get('author')
                environ.set_env('JESSY_AUTHOR', self.author)

            if data.get('settings'):
                self.settings = SourceFileLoader("settings",
                                                 data.get('settings')) \
                                .load_module()

                if hasattr(self.settings, 'DATABASE'):
                    self.connection = Connection(self.settings)
                    self.command = Command(self.connection)
                    #where = sql_text.add_condition(
                    #    ((Condition.AND, 'jessy', 'name', Operation.EQUAL),
                    #     (Condition.OR, 'jessy', 'id', Operation.EQUAL),)
                    #)

                    #print(self.command.select(('name', ), 'jessy',
                    #                condition= (where),
                    #                params=('he', 1)).all()
                    #      )

                    #self.command.insert(('name',), 'jessy',
                    #                    params=('di',))

                    #print(self.command.last_id)

                    #where = sql_text.add_condition(
                    #    ((Condition.OR, 'jessy', 'id', Operation.EQUAL),)
                    #)
                    #print(self.command.last_id)


                    #ret = self.command.delete(
                    #    'jessy',
                    #    condition= (where),
                    #    params=(8,)
                    #)

                    #print(ret)

                    #ret = self.command.update(('name',),
                    #                    'jessy',
                    #                    condition= (where),
                    #                    auto_commit=False,
                    #                    params= ('hella', 11))

                    #print(ret)

                if hasattr(self.settings, 'PROGRAM_DEBUG'):
                    environ.set_env('JESSY_PROGRAM_DEBUG',
                                    str(self.settings.PROGRAM_DEBUG))
            else :
                print('settings.py has not found')
                return


    def loadEnv(self):
        environ.loadEnv('default.env')


    def get_command(self):
        if hasattr(self.settings, 'DATABASE'):
            return self.command
        else:
            print('Database has not found in settings.py')
            return None


    def get_connection(self):
        if hasattr(self.settings, 'DATABASE'):
            return self.connection
        else:
            print('Database has not found in settings.py')
            return None
