from fabric.api import local, settings, abort
from fabric.contrib.console import confirm


# prepare for deployment

def test():
    local("nosetests -v")


def commit():
    message = raw_input("Enter a git commit message: ")
    local("git add . && git commit -am'{}'".format(message))


def push():
    local("git push originmaster")

def prepare():
    test()
    commit()
    push()