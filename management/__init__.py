import os
import sys
from argparse import ArgumentParser
import collections
import importlib


def get_extern_commands_dict(management_dir):
    """
    List the names in management/commands, without .py

    return  {cmd_name: app, ...}
    """
    commands_dir = os.path.join(management_dir, 'commands')
    try:
        commands =  [f[:-3] for f in os.listdir(commands_dir)
                     if not f.startswith('_') and f.endswith('.py')]
        # This commands are all in management app
        return {cmd: 'management' for cmd in commands}
        
    except OSError:
        return {}
        


class BoskArgumentParser(ArgumentParser):
    """
    Print external commands
    """
        
    def print_help(self):
        ArgumentParser.print_help(self)
        
        # Print extern commands help
        usage = ["",
                 "Valid commands list blew:",]
        commands = get_extern_commands_dict(__path__[0])
        commands_ddict = collections.defaultdict(lambda: [])
        for cmd in sorted(commands.keys()):
            commands_ddict[commands[cmd]].append(cmd)

        for app in sorted(commands_ddict.keys()):
            usage.append("")
            usage.append("[%s]" % app)
            for cmd in sorted(commands_ddict[app]):
                usage.append("    %s" % cmd)

        sys.stdout.write('\n'.join(usage))
        

class ManagementUtil():
    """
    Encapsulates the logic of management utilities.
    """
    def __init__(self):
        self.argv = sys.argv
        self.prog_name = os.path.basename(self.argv[0])
        
        
    def run(self):
        parser = BoskArgumentParser()
        parser.add_argument('command', help='Bosk top level commnad')
        parser.add_argument('-v', '--verbose', help='Show verbose information')
        parse_dict = vars(parser.parse_args(self.argv[1:]))
        
        self.fetch_command(parse_dict['command']).run(**parse_dict)


    def fetch_command(self, command):
        extern_commands = get_extern_commands_dict(__path__[0])
        try:
            app_name = extern_commands[command]
        except KeyError:
            sys.stderr.write("Unknown command: %s\n" % command)
            sys.exit(1)

        mod = importlib.import_module('bosk.management.commands.%s' % command)
        return mod.Command()

            
def run_commands():
    util = ManagementUtil()
    util.run()
