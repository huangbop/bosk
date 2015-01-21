import os
import sys
import random
import string

import bosk
from bosk.management.commands.base import BaseCommand


class Command(BaseCommand):
    """
    """

    def run(self, **parse_dict):
        print('Create project ...')
                    
        project_name = parse_dict.get('name', ''.join(random.sample(string.ascii_letters, 8)))
        project_dir = os.path.join(os.getcwd(), project_name)
        try:
            os.makedirs(project_dir)
        except OSError:
            # print('Create "%s" failed.' % project_dir)
            # sys.exit(1)
            pass

        # Copy main project templates
        template_dir = os.path.join(bosk.__path__[0], 'conf', 'project_template')
        # Compute the relative portion
        prefix_len = len(template_dir) + 1 # strip start slash 

        import pdb; pdb.set_trace()
        for root, dirs, files in os.walk(template_dir):
            valid_part = root[prefix_len:]
            for dirname in dirs:
                try:
                    dir_path = os.path.join(project_dir, valid_part, dirname)
                    print(dir_path)
                    os.makedirs(dir_path)
                except OSError:
                    # print('Create dir %s failed.' % dir_path)
                    # exit(1)
                    pass
            for filename in files:
                old_path = os.path.join(root, filename)
                new_path = os.path.join(project_dir, valid_part, filename)

                with open(old_path, 'rb') as temp_file:
                    content = temp_file.read()
                    with open(new_path, 'wb') as write_file:
                        write_file.write(content)


        
        BaseCommand.run(self, **parse_dict)


        
