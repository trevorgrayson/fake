# fake

fake gives you a way to manage the life cycle of your application without getting bogged down with the syntax.

Whether you `rails s` or `./manage.py runserver`, you can stop abusing your shell history and use this single interface:

```
    fake server 
```
## Commands
```
    fake server
    fake test

    fake create
    fake migrate
```

## Installation

clone this repo and add it's bin folder to your path. /opts/ is a good folder to install to, if you wish.

```
  git clone git@github.com:trevorgrayson/fake.git
  export PATH="`pwd`/fake:$PATH"
```

Add the `export PATH` command using an absolute path to your .bash_profile if you want it to work when you restart your terminal.
