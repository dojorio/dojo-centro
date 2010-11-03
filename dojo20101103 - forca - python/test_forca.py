"""
>>> from forca import JogoDaForca
>>> forca = JogoDaForca("casa")
>>> str(forca)
'----'
>>> forca.erros
0
>>> forca.tente('c')
>>> str(forca)
'c---'
>>> forca.tente('b')
>>> forca.erros
1
>>> forca.tente('x')
>>> forca.erros
2
>>> forca.tente('z')
>>> forca.erros
3
>>> forca.tente('s')
>>> str(forca)
'c-s-'
>>> forca.tente('a')
>>> str(forca)
'casa'
>>> forca = JogoDaForca('casa')
>>> forca.tente('a')
>>> str(forca)
'-a-a'

"""

import doctest

if __name__ == "__main__":
    doctest.testmod()

