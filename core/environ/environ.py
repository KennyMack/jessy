#!/usr/bin/python3
import os
import re


def loadEnv(path):
    try:
        with open(path) as f:
            content = f.read()
            for line in content.splitlines():
                envMatch = re.match(r'\A([A-Za-z_0-9]+)=(.*)\Z', line)
                if envMatch:
                    key, val = envMatch.group(1), envMatch.group(2)
                    envMatchValA = re.match(r"\A'(.*)'\Z", val)
                    if envMatchValA:
                        val = envMatchValA.group(1)
                    envMatchValB = re.match(r'\A"(.*)"\Z', val)
                    if envMatchValB:
                        val = re.sub(r'\\(.)', r'\1', envMatchValB.group(1))
                    set_env(key, val)
    except IOError:
        content = ''


def get_env(key):
    return os.environ.get(key)


def set_env(key, value):
    os.environ.setdefault(key, value)
