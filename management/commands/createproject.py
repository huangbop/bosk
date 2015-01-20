import os
import sys


from bosk.management.commands.base import BaseCommand


class Command(BaseCommand):
    """
    """

    def run(self, **parse_dict):
        print('Create project ...')
                    
        project_dir = os.path.join(os.getcwd(), '?bosk_project')
        try:
            os.makedirs(project_dir)
        except OSError:
            print('Create "%s" failed.' % project_dir)
            sys.exit(1)

        # Copy main project templates
        
        
        BaseCommand.run(self, **parse_dict)


        
