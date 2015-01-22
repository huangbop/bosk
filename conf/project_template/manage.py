#!python
import os
import sys

from bosk.management import run_commands


if __name__ == '__main__':
    os.environ.setdefault('BOSK_SETTING_MODULE', 'project.setting')
    run_commands()
