#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""Usage:
    gitinit.py [-h | --help]
    gitinit.py [-n <username> | --name <username>] [-e <email> | --email <email>] <path>
    gitinit.py <path>

-h --help   display help and exit
-n --name   git config user.name (local)
-e --email  git config user.email (local)
path        path to the directory to create the repo
"""

import os
import sys
import argparse
import logging
from docopt import docopt

#specific import for git
import git
# file adding and http
import glob
import requests

__author__ = "Alexander O'Connor <Alex.OConnor@scss.tcd.ie>"
__copyright__ = "Copyright 2014, Alexander O'Connor <Alex.OConnor@scss.tcd.ie>"
__credits__ = ["Alexander O'Connor <Alex.OConnor@scss.tcd.ie>"]
__license__ = "Copyright"
__version__ = "0.1"
__email__ = "Alexander O'Connor <Alex.OConnor@scss.tcd.ie>"
__status__ = "Prototype"

#Create project files
files = {
    'README.md' : "# README \n The new README for the project \n",
    'dotgitignore' : "http://www.gitignore.io/api/linux,vim,osx,python",
}


def createFiles(path):
    '''create basic files including the .gitignore and readme BEFORE the repo is made'''
    for filename in files:
        with open(filename.replace('dot','.'), 'w') as FILE:
            if files[filename].startswith('http'):
                r = requests.get(files[filename])
                FILE.write(r.text)
                print 'wrote %s from http' % filename
            else:
                FILE.write(files[filename])
                print 'wrote %s' % filename

def addFilesAndCommit(repo, path):
    '''at the end, add the files starting with the gitignore and readme'''
    for filename in files:
        print 'added %s' % filename.replace('dot','.')
        repo.index.add([filename.replace('dot','.')])
    #add python files. I ran into a problem with accidentally adding .git otherwise
    for filename in glob.iglob(os.path.join(path,'*.py')):
        repo.index.add([filename])
        print 'added %s' % filename

    repo.index.commit('initial commit; automatically created repo and added files. need to add upstream')

def userConfig(username, email, repo):
    '''locally set the username and email'''
    config = repo.config_writer()
    config.set_value('user', 'email', email)
    config.set_value('user', 'name', username)
    print 'set %s <%s>' % (username, email)

def createRepo(path):
    '''access the repo'''
    #bare means create the contents of .git
    return git.Repo.init(path, bare=False)

if __name__ == '__main__':
    arguments = docopt(__doc__, version=__version__)

    print arguments

    if not arguments['<path>']:
        arguments['<path>'] = os.getcwd()
        print 'using current working directory as path %s' % arguments['<path>']
    if not (arguments['<email>'] and arguments['<name>']):
        arguments['<email>'] = 'Alex.OConnor@scss.tcd.ie'
        arguments['<name>'] = 'Alex O\'Connor'
        print 'using default username and email: %s : <%s>' % (arguments['<name>'], arguments['<email>'])

    createFiles(arguments['<path>'])
    #create the repo
    repo = createRepo(arguments['<path>'])
    userConfig(arguments['<name>'], arguments['<email>'], repo)
    addFilesAndCommit(repo, arguments['<path>'])
