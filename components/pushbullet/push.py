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
import yaml

from docopt import docopt

logger = logging.getLogger(__name__)


class PushBullet:
    def __init__(self):
        self.configure_logging()

        self.data = []
        self.cache_file = 'pickled.data'
        self.yaml_file = 'data.yml'

    def process(self):
        self.arguments = docopt(__doc__, version='PushBullet 0.1')
        logger.info('PushBullet started...')

        loaded_stream = self.load_yaml(self.yaml_file)
        if loaded_stream is None:
            logger.info('Previous data does not exist')
        else:
            logger.info('Loaded data')
        pass

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

    def save_yaml(self, expressions):
        with open(self.yaml_file, 'w') as outfile:
            outfile.write(yaml.dump(expressions, default_flow_style=False))

    def load_yaml(self, yaml_file):
        if os.path.exists(yaml_file):
            stream = open(yaml_file, 'r')
            return yaml.load(stream)
        else:
            return None


    def log(self):
        pass

def test_something():
    push_bullet = PushBullet()
    push_bullet.create_record()
    assert(True)


if __name__ == "__main__":
    print "Running PushBullet in stand-alone-mode"

    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    push_bullet = PushBullet()
    push_bullet.process()

