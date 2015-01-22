









def restart_with_reloader():
    while True:
        



def python_reloader(main_func, *args, **kwargs):
    try:
        exit_code = restart_with_reloader()

    except:
        pass





def main(main_func, *args, **kwargs):
    reloader = python_reloader

    python_reloader(main_func, *(), **{})

    
