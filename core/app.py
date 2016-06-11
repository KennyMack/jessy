#!/usr/bin/python3
from core.environ import environ
from importlib.machinery import SourceFileLoader
import json


class Application(object):
    def __init__(self, path):
        with open(path) as data_file:
            data = json.load(data_file)

            environ.set_env('JESSY_PROGRAM_DEBUG', 'True')

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
                self.settings = SourceFileLoader("settings", data.get('settings')).load_module()

                if hasattr(self.settings, 'DATABASE'):
                    print(self.settings.DATABASE)

                if hasattr(self.settings, 'PROGRAM_DEBUG'):
                    environ.set_env('JESSY_PROGRAM_DEBUG', str(self.settings.PROGRAM_DEBUG))

    def loadEnv(self):
        environ.loadEnv('default.env')
