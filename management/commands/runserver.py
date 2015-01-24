import os
import sys
import subprocess
import time
from threading import Thread
from wsgiref import simple_server


def application(environ, start_response):
    """
    """
    start_response('200 OK', [])
    
    return [b'xxx']

def start_serve():

    httpd = simple_server.WSGIServer(('', 8000), simple_server.WSGIRequestHandler)

    httpd.set_app(application)

    httpd.serve_forever()
    



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
            
