import os

def is_django():
    return os.path.isfile('manage.py')

def is_rails():
    return os.path.isfile('config.ru')
    
