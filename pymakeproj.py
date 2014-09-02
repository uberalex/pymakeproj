#!/usr/bin/python

# -*- coding: utf-8 -*-

"""Usage:
    pymakeproj.py [-h | --help]
    pymakeproj.py [-f | --file] [--author <authorname>] (<filename>)
    pymakeproj.py [--author <authorname>] (<filename>)
    pymakeproj.py [-f | --file] (<filename>)
    pymakeproj.py <filename>

-h --help    display help or exit
-f --file    just create a file, not a directory
--author     author string other than the default
filename     project / filename (.py will be added)
"""

import os
import sys
from docopt import docopt

__author__ = "Alexander O'Connor"
__copyright__ = "Copyright 2012, Alexander O'Connor"
__credits__ = ["Alexander O'Connor"]
__license__ = "Copyright"
__version__ = "0.1"
__email__ = "oconnoat@gmail.com"
__status__ = "Production"

strings = { 'pythonheader' : u'#!/usr/bin/python\n\n# -*- coding: utf-8 -*-\n\n',
            'docopt' : u'""" docstring """\n\n',
            'imports' : u'import os \nimport sys\n\n',
            'docstring' : u'''
__author__ = "{0}"
__copyright__ = "Copyright 2012, {0}"
__credits__ = ["{0}"]
__license__ = "Copyright"
__version__ = "0.1"
__email__ = "{0}"
__status__ = "Prototype"\n\n
''',
            'main' : u'if __name__ == \'__main__\':\n'}

if __name__ == '__main__':
    arguments = docopt(__doc__, version=__version__)

    print arguments

    if arguments['<filename>']:
        if not arguments['<authorname>']:
            arguments['<authorname>'] = 'Alexander O\'Connor <oconnoat@gmail.com>'
        if not arguments['--file']:
            print 'Creating the directory and main file'

            try:
                if not os.path.exists(arguments['<filename>']):
                    #actually make the directory
                    os.makedirs(arguments['<filename>'])
                    #create the main file
                    with \
                    open(os.path.join(arguments['<filename>'],arguments['<filename>']+'.py'),'w') as mainfile:
                        mainfile.write(strings['pythonheader'])
                        mainfile.write(strings['docopt'])
                        mainfile.write(strings['imports'])
                        mainfile.write(strings['docstring'].format(arguments['<authorname>']))
                        mainfile.write(strings['main'])

                else:
                    raise Exception('Directory already exists.')

            except Exception,e:
                print 'error',e


        else:
            print 'Creating file'
            if not os.path.exists(arguments['<filename>']+'.py'):
                #create the main file
                with \
                open(arguments['<filename>']+'.py','w') as pyfile:
                    pyfile.write(strings['pythonheader'])
                    pyfile.write(strings['imports'])
                    pyfile.write(strings['docstring'].format(arguments['<authorname>']))
