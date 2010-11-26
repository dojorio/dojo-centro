#-*- coding: utf-8 -*-
"""


Dojotools - tools for your coding dojo session

Copyright (C) 2009 Flávio Amieiro <amieiro.flavio@gmail.com>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; version 2 dated June, 1991.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Library General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, see <http://www.gnu.org/licenses/>.

If you find any bugs or have any suggestions email: amieiro.flavio@gmail.com
"""

import os
import sys
import subprocess
from optparse import OptionParser
from time import sleep, ctime

try:
    import pynotify
except ImportError:
    pynotify = None
    print
    print
    sys.stderr.write('*** Could not import pynotify. Make sure it is installed so you can see the notifications ***\n')
    print
    print


def run_command(directory, test_cmd):
    """
    As the name says, runs a command and wait for it to finish
    """
    process = subprocess.Popen(
        test_cmd,
        shell = True,
        cwd = directory,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
    )

    output = process.stdout.read()
    output += process.stderr.read()
    status = process.wait()

    sys.stdout.write(output)

    if pynotify:
        pynotify.init('dojotools')
        message = pynotify.Notification('Dojotools', output)

        message.set_urgency(pynotify.URGENCY_NORMAL if status == 0 else pynotify.URGENCY_CRITICAL)

        message.show()


def git_commit_all(directory):
    """
    Adds all files and commits them
    """
    msg = ctime()
    process = subprocess.Popen(
        "git add .; git commit -m '%s'" % msg,
        shell=True,
        cwd=directory,
    )

    #if git returns 128 it means 'command not found' or 'not a git repo'
    if process.wait() == 128:
        error = 'Impossible to commit to repository. ' + \
                'Make sure git is installed an this is a valid repository'
        raise OSError(error)


def filter_files(files, patterns):
    """
    Filter a list of strings based on each item in 'patterns'

    Be careful, 'patterns' is NOT a regex, we only test if the string
    *contains* each of the so called patterns
    """
    for p in patterns:
        files = [f for f in files if p not in f]
    return files


def monitor(directory, functions, patterns):
    """
    Monitor a directory for changes, ignoring files matching any item in patterns and calls
    any func in functions when a file was changed.

    functions must be a list of tuples, each of which contains
    as their first item the function to be called. Whatever remains
    will be passed as arguments. For example:

    If your function list is this:

        > functions = [(my_func, 1, 2, 3)]

    then the result would be calling my_func with 1, 2 and 3 as args

        > myfunc(1, 2, 3)

    """
    old_sum = 0
    while True:

        m_time_list = []
        for root, dirs, files in os.walk(directory):
            # I have to ignore all the files in .git dir because
            # any commit changes them considering them would cause
            # an infinite loop
            if '.git' in root:
                continue
            files = filter_files(files, patterns)
            # Be careful. The += operator works as the extend method
            # on mutable objects. For more information refer to
            # http://zephyrfalcon.org/labs/python_pitfalls.html
            m_time_list += [
                os.stat(os.path.join(root, f)).st_mtime for f in files
            ]

        new_sum = sum(m_time_list)
        if new_sum != old_sum:
            for function in functions:
                function[0](*function[1:])
            old_sum = new_sum

        sleep(1)


def parse_options():
    usage = "%prog [OPTIONS] COMMAND ..."
    description = """
        %prog watches a directory for changes. As soon as there are any changes
        to the files being watched, it runs the commands specified as positional
        arguments. You can specify as many commands as you wish, but don't forget
        to use quotes if you command has spaces in it.
    """.replace('  ', '')
    parser = OptionParser(usage, description=description)
    parser.add_option(
        '-d',
        '--directory',
        action = 'store',
        type = 'string',
        dest = 'directory',
        help = 'Watch DIRECTORY',
        metavar = 'DIRECTORY',
        default = os.path.abspath(os.path.curdir)
    )

    parser.add_option(
        '-c',
        '--commit',
        action='store_true',
        dest = 'commit',
        help = ' '.join([
            'if this flag is used, a git commit will',
            'be issued whenever the files change'
        ]),
    )

    parser.add_option(
        '-p',
        '--pattern',
        action = 'append',
        type = 'string',
        dest = 'patterns',
        help = ' '.join([
            'Ignore PATTERN.',
            'You may define this as many times as you want',
            'like in -p .txt -p .swp'
            ]),
        metavar = 'PATTERN',
        default = [],
    )
    return parser.parse_args()


if __name__ == '__main__':

    options, args = parse_options()

    try:
        print 'Monitoring files in %s' % options.directory
        if options.patterns:
            print 'ignoring files with %s in their name' % ' '.join(options.patterns)
        print 'press ^C to quit'

        functions = []

        if options.commit:
            functions.append((git_commit_all, options.directory))

        for command in args:
            functions.append((run_command, options.directory, command))

        monitor(options.directory, functions, options.patterns)

    except KeyboardInterrupt:
        print '\nleaving...'
        sys.exit(0)
