import os
import sys
from argparse import ArgumentParser


def find_extern_commands(management_dir):
    """
    List the names in management/commands, without .py
    """
    commands_dir = os.path.join(management_dir, 'commands')
    try:
        pass
    except OSError:
        return []
    
    

    




class BoskArgumentParser(ArgumentParser):
    """
    Print external commands
    """
        
    def print_help(self):
        ArgumentParser.print_help(self)
        print('\nI stand here')
        


class ManagementUtil():
    """
    Encapsulates the logic of management utilities.
    """
    def __init__(self):
        self.argv = sys.argv
        
        
    def run(self):
        parser = BoskArgumentParser()
        parser.add_argument('command', help='Bosk top level commnad')
        parser.add_argument('-v', '--verbose', help='Show verbose information')
        command_dict = vars(parser.parse_args(self.argv[1:]))

            
def run_commands():
    util = ManagementUtil()
    util.run()
