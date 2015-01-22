import os
import sys
import subprocess
import time
from threading import Thread


def start_serve():
    for i in range(10):
        print(i)



class Command():
    """
    """

    def run(self, **argv):
        print('Run server ...')
        env_ = os.environ.copy()
        if env_.get('BOSK_SUBPROCESS') == 'true':
            # run in sub process
            # start new thread here
            server_thread = Thread(target=start_serve)
            server_thread.start()
        else:
            # run in main process, spawn it.
            env_['BOSK_SUBPROCESS'] = 'true'
            retval = subprocess.call('python manage.py runserver', env=env_)
            
