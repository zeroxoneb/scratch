#!/usr/bin/env python3

import argparse

class Command(object):
    @classmethod
    def names(cls):
        return []

    def execute(self):
        print('{}.execute()'.format(self.__class__.__name__))

class SubCommand(Command):

    @classmethod
    def names(cls):
        return ['sub']

class NamedCommand(Command):

    @classmethod
    def names(cls):
         return ['name', 'named']


def main():

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand', help='Which command to execute')

    
