from pprint import pprint

def gerador_de_acumulador_feio(n):
    n = [n]
    def prototipo_de_acumulador(i):
        pprint(locals())
        locals()['n'] += ["adiciona ai!"]
        
        n[0] += i
        return n[0]
    return prototipo_de_acumulador
   
'''
;; common lisp

(defun acumulador (n)
    (lambda (i) (incf n i)))
'''

def gerador_de_acumulador_bonito(n):
    # lambda i: n += i
    # i => n += i
    global b
    b = n
    def prototipo_de_acumulador(i):
        global b
        n = b + i
        return n
    return prototipo_de_acumulador

acumulador = gerador_de_acumulador_feio(5)
assert acumulador(1) == 6
assert acumulador(-1) == 5
assert acumulador(4) == 9
assert acumulador(7) == 16
