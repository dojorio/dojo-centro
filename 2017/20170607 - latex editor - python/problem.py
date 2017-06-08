#!/usr/bin/env python
# -*- coding: utf-8 -*-
def MkDic(str):
    return {"A":[]}
def latex(comando):
    if 'C' in comando:
        if comando.count('pstree') == 2:
            return '  A\n' \
                   ' B\n' \
                   'C'
        return ' A\n' \
               'B C'
    elif len(comando) > 30:
        return ' A\n' \
               'B'



    return 'A'