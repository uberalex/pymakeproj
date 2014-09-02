#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""Usage:
    gitinit.py <filename>

filename     project / filename (.py will be added)
"""

import os
import sys
import argparse
import logging
from docopt import docopt

#specific import for git
import git

__author__ = "Alexander O'Connor <Alex.OConnor@scss.tcd.ie>"
__copyright__ = "Copyright 2014, Alexander O'Connor <Alex.OConnor@scss.tcd.ie>"
__credits__ = ["Alexander O'Connor <Alex.OConnor@scss.tcd.ie>"]
__license__ = "Copyright"
__version__ = "0.1"
__email__ = "Alexander O'Connor <Alex.OConnor@scss.tcd.ie>"
__status__ = "Prototype"

filecontents = {'.gitignore':
                            u'''#Some of this from https://github.com/github/gitignore

#OS files and Swap Files
*~
*.lock
*.DS_Store
*.swp
*.out

#Vim
[._]*.s[a-w][a-z]
[._]s[a-w][a-z]
*.un~
Session.vim
.netrwhist
*~

#Python
__pycache__/
*.py[cod]''',
                'README.md':
                            u'#Blank Example README'}

def git_init(repo_path):
    repo = git.Repo(repo_path)
    assert repo.bare == False
    repo.git.init()
    index = repo.git.index()
    for filename in filecontents:
        with open(os.path.join(repo_path,filename), 'wb') as pyfile:
            pyfile.write(filecontents[filename])
        index.add(os.path.join(repo_path,filename))

    index.commit('initial commit, gitignore and readme')

if __name__ == "__main__":
    arguments = docopt(__doc__, version=__version__)
    if not arguments['<filename>']:
        arguments['<filename>'] = os.getcwd()

    print 'using path: %s' % (arguments['<filename>'])
    git_init(arguments['<filename>'])
