#!/usr/bin/env python

"""PushBullet

Supports the creation of Advice Wizards


Usage:
   push_bullet.py idea <idea>

Options:
    -h --help     Show this screen.
    --version     Show version.

"""

__author__ = "Indika Piyasena"


import os, sys
import logging
import pickle

from docopt import docopt
from pushbullet import PushBullet


logger = logging.getLogger(__name__)


class PushBulletWrapper:
    def __init__(self):
        self.configure_logging()

        self.data = []
        self.cache_file = 'pickled.data'

    def process(self):
        self.arguments = docopt(__doc__, version='PushBulletWrapper 0.1')
        logger.info('PushBulletWrapper started...')

        apiKey = "ff309eaf3af91efbbfbe590c7fcac464"
        p = PushBullet(apiKey)
        # p = PushBullet(apiKey)
        # Get a list of devices
        devices = p.getDevices()

        # Send a note
        p.pushNote(devices[0]["id"], 'Hello world', 'Test body')


    def configure_logging(self):
        logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        pass

    def pickle(self):
        # Simple dump and load paradigm
        file_pi = open(self.cache_file, 'w')
        pickle.dump(self.data, file_pi)

    def revive(self):
        file_pi = open(self.cache_file, 'r')
        self.data = pickle.load(file_pi)


    def log(self):
        pass

def test_something():
    push_bullet = PushBulletWrapper()
    push_bullet.create_record()
    assert(True)


if __name__ == "__main__":
    print "Running PushBulletWrapper in stand-alone-mode"

    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    push_bullet = PushBulletWrapper()
    push_bullet.process()

