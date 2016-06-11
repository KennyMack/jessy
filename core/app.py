#!/usr/bin/python3
from core.environ import environ

class Application(object):
    def __init__(self, name):
        self._name = name
        environ.set_env('JESSY_APPNAME', self._name)

    def loadEnv(self):
        environ.loadEnv('envVars.env')
