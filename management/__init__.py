import os
import sys
import argparse

class ManagementUtil():
    """
    Encapsulates the logic of management utilities.
    """
    def __init__(self):
        self.argv = sys.argv
        
    def run(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--verbose', nargs='?',help='verbose' )
        parser.add_argument('command', nargs='*')
        parser.add_argument('-v', '--verbosex', help='Show verbose information')
        parser.parse_args()


def run_commands():
    util = ManagementUtil()
    util.run()
