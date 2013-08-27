#!/usr/bin/python

"""Remap

Remaps Sublime keymap files between OSX and Windows

"""

__author__ = "Indika Piyasena"


import os, sys, glob
import logging
import fileinput

logger = logging.getLogger(__name__)

def mtime(filename):
    return os.stat(filename).st_mtime

def atime(filename):
    return os.stat(filename).st_atime


class Remap:
    def __init__(self):
        self.configure_logging()
        self.sublime_win_file = 'Default (Windows).sublime-keymap'
        self.sublime_osx_file = 'Default (OSX).sublime-keymap'

    def process(self):
        self.last_file_updated()
        pass

    def last_file_updated(self):
        query = '*.sublime-keymap'
        keymap_files = glob.glob(query)

        sorted_files = sorted(keymap_files, key=mtime, reverse=1)
        last_modified_file = sorted_files[0]
        second_last_modified_file = sorted_files[1]

        t1 = mtime(last_modified_file)
        t2 = mtime(second_last_modified_file)

        logger.debug('Last modified time: {0}'.format(t1))
        logger.debug('Second Last modified time: {0}'.format(t2))

        if abs(t1 - t2) < 0.1:
            logger.info('Both files are timestamp equal')
        else:
            last_modified_time = mtime(last_modified_file)
            last_access_time = atime(last_modified_file)

            # So, is this the Windows file or the OSX file?
            if last_modified_file == 'Default (Windows).sublime-keymap':
                self.regenerate_osx(last_access_time, last_modified_time)

            if last_modified_file == 'Default (OSX).sublime-keymap':
                self.regenerate_windows(last_access_time, last_modified_time)
        pass

    def regenerate_windows(self, with_access_timestamp, with_modified_timestamp):
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

        os.utime(self.sublime_win_file, (with_access_timestamp, with_modified_timestamp))

    def regenerate_osx(self, with_access_timestamp, with_modified_timestamp):
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

        os.utime(self.sublime_osx_file, (with_access_timestamp, with_modified_timestamp))

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
