from subprocess import call

def server():
    call(['rails','s'])

def migrate():
    call(['rake', 'db:migrate'])

def create():
    call(['rake', 'db:create'])

def test():
    call(['rspec'])
