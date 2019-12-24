# -*- coding: utf-8 -*-

# pylint: disable-msg=no-name-in-module,import-error
from distutils.cmd import Command
from os import getcwd
from subprocess import check_call
from setuptools import setup

class PylintCommand(Command):
    description = 'run pylint on Python source files'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        command = ['pylint', getcwd()]
        return check_call(command)

class NosetestCommand(Command):
    description = 'run nosetests on Python source files'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        command = ['nosetests', '--verbose', '--config', 'tests/setup.cfg']
        return check_call(command)

setup(cmdclass={
    'lint': PylintCommand,
    'test': NosetestCommand
})
