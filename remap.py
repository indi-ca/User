#!/usr/bin/python

"""Remap

Remaps Sublime keymap files between OSX and Windows


Usage:
   remap.py regenerate <config>

Options:
    -h --help     Show this screen.
    --version     Show version.

"""

__author__ = "Indika Piyasena"


import os, sys, glob
import logging
import fileinput
from docopt import docopt

logger = logging.getLogger(__name__)

def mtime(filename):
    return os.stat(filename).st_mtime


class Remap:
    def __init__(self):
        self.configure_logging()
        self.arguments = docopt(__doc__, version='Remap 0.1')
        self.sublime_win_file = 'Default (Windows).sublime-keymap'
        self.sublime_osx_file = 'Default (OSX).sublime-keymap'

    def process(self):
        self.last_file_updated()
        #self.regenerate_osx()
        pass

    def last_file_updated(self):
        # A list of 'sublime-keymap' files
        # Their last updated timestamp
        # The one which was updated last, is the source file
        query = '*.sublime-keymap'
        keymap_files = glob.glob(query)

        sorted_files = sorted(keymap_files, key=mtime, reverse=1)
        last_modified_file = sorted_files[0]

        # So, is this the Windows file or the OSX file?
        if last_modified_file == 'Default (Windows).sublime-keymap':
            self.regenerate_osx()

        if last_modified_file == 'Default (OSX).sublime-keymap':
            self.regenerate_windows()

        pass


    def regenerate_windows(self):
        logger.info('Generating Windows Configuration File')
        logger.info('aka... converting OSX -> Windows')

        if os.path.exists(self.sublime_win_file):
           os.unlink(self.sublime_win_file)

        with open(self.sublime_win_file, 'w') as w:
            with open(self.sublime_osx_file, 'r') as f:
                for line in f:
                    newline = line.replace("super", "SWAP_VARIABLE")
                    newline = newline.replace("ctrl", "super")
                    newline = newline.replace("SWAP_VARIABLE", "ctrl")
                    w.write(newline)


    def regenerate_osx(self):
        logger.info('Generating OSX Configuration File')
        logger.info('aka... converting Windows -> OSX')

        if os.path.exists(self.sublime_osx_file):
           os.unlink(self.sublime_osx_file)

        with open(self.sublime_osx_file, 'w') as w:
            with open(self.sublime_win_file, 'r') as f:
                for line in f:
                    newline = line.replace("ctrl", "SWAP_VARIABLE")
                    newline = newline.replace("super", "ctrl")
                    newline = newline.replace("SWAP_VARIABLE", "super")
                    w.write(newline)


    def configure_logging(self):
        logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        pass


if __name__ == "__main__":
    print "Running Remap in stand-alone-mode"
    wizardry = Remap()
    wizardry.process()
