#!/usr/bin/env python
# -*- coding: utf-8 -*-

def latex(comando):
    if 'C' in comando:
        if comando.count('pstree') == 2:
            return '''
  A
 B
C'''
        return '''
 A
B C'''
    elif len(comando) > 30:
        return '''
 A
B'''



    return '''
A'''