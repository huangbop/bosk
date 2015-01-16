import os
import sys
import argparse

class ManagementUtil():
    """
    Encapsulates the logic of management utilities.
    """
    def __init__(self):
        self.argv = sys.argv

    def add_intern_commands(self, parser):
        parser.add_argument('--command', help='Top level command')
        

    def run(self):
        parser = argparse.ArgumentParser()
        self.add_intern_commands(parser)
        commands_dict = None
        try:
            commands_dict = vars(parser.parse_args(self.argv[1:]))
        except:                 # Catch sys exit
            pass

        if len(self.argv) < 2:
            parser.print_help()

        print(commands_dict)
        
            


def run_commands():
    util = ManagementUtil()
    util.run()
