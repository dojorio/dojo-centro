#!/usr/bin/env python
import os
import sys
from collections import defaultdict
#from pprint import pprint

def merge_by_language(languages_dict, dojo):
    languages_dict[dojo.get('language', '?')].append(dojo)
    return languages_dict

def to_dojo(string):
    parts = string.split(' - ')
    if len(parts) == 3:
        date, problem, language = parts
        return dict(date=date, problem=problem, language=language)
    return dict(date=parts[0])

def dojos_by_language(dir):
    return dict(reduce(merge_by_language,
                       (to_dojo(x) for x in sorted(os.listdir(dir)) if x[0].isdigit()), defaultdict(list)))

if __name__ == '__main__':
    #pprint(dojos_by_language('2010'))
    if len(sys.argv) == 2:
        result = dojos_by_language(sys.argv[1])
        for language in sorted(result.keys()):
            print '-- %s (%d) %s' % (language, len(result[language]), '-'*(70 - len(language)))
            for dojo in result[language]:
                print '%s: %s' % (dojo['date'], dojo.get('problem', '?'))
            print
    else:
        print "USAGE: %s [directory]\nPrints information about dojos in that directory." % sys.argv[0]
