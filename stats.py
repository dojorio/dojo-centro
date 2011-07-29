#!/usr/bin/env python
# Author: Rodolfo Henrique Carvalho
# This is in public domain.

import os
import sys
from collections import defaultdict


def dirname_to_dojo(dirname):
    """Return a dojo from a string representation.
    
    `dirname': "YYYYMMDD[ - problem name - language name]"
    `dojo': dict(date) or dict(date, problem, language)
    """
    parts = dirname.split(' - ', 2)
    if len(parts) == 3:
        date, problem, language = parts
        return dict(date=date, problem=problem, language=language)
    else:
        return dict(date=parts[0])


def dojos_from_dir(dirpath):
    """Return a list of dojos in dirpath.
    
    A `dojo' is a directory contained in dirpath that starts
    with a digit (for the date).
    """
    pth = dirpath
    dtd = dirname_to_dojo
    ls, isdir, jn = os.listdir, os.path.isdir, os.path.join
    isdig = str.isdigit
    cond = lambda x: isdir(jn(pth, x)) and isdig(x[0])
    return [dtd(x) for x in ls(pth) if cond(x)]


def group_by_language(dojos):
    """Return a dictionary of dojos grouped by languages."""
    def append_to_language_group(dikt, dojo):
        dikt[dojo.get('language', '?')].append(dojo)
        return dikt
    return dict(reduce(append_to_language_group, dojos, defaultdict(list)))


def print_dojos_by_language(dojos):
    groups = group_by_language(dojos)
    for language in sorted(groups.keys(), key=lambda lang: (-len(groups[lang]), lang)):
        print '-- %s (%d) %s' % (language, len(groups[language]), '-'*(70 - len(language)))
        for dojo in sorted(groups[language]):
            print '%s: %s' % (dojo['date'], dojo.get('problem', '?'))
        print

def print_dojos_by_language_summary(dojos):
    groups = group_by_language(dojos)
    print "Linguagem\t# dojos"
    for language in sorted(groups.keys(), key=lambda lang: (-len(groups[lang]), lang)):
        print '%s\t%d' % (language, len(groups[language]))

if __name__ == '__main__':
    dirs = set(sys.argv[1:])
    help_ops = ["-h", "--help"]
    short_ops = ["-s", "--short"]
    
    if not dirs or dirs.intersection(help_ops):
        usage = ("Prints information about dojos in directories.\n"
                 "USAGE: %s [options] DIRECTORY [DIR2] [DIR3] ...\n"
                 "Options:\n"
                 " %-16s                show this help\n"
                 " %-16s                show only a summary"
                 % (sys.argv[0],
                    ' , '.join(help_ops),
                    ' , '.join(short_ops)))
        print >>sys.stderr, usage
        sys.exit(1)
    else:
        dojos = []
        
        if dirs.intersection(short_ops):
            print_ = print_dojos_by_language_summary
            dirs.difference_update(short_ops)
        else:
            print_ = print_dojos_by_language
        
        while dirs:
            dojos.extend(dojos_from_dir(dirs.pop()))
        
        print_(dojos)

