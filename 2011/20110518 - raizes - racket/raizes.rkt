#lang racket
(require rackunit)

(define (± a)
  (list (- a) a)) 

(define (raízes a b c)
  (let* ((b² (* b b))
         (delta (- b² (* 4 c a))))
    (/ (± (- b) (sqrt delta)) (* 2 a))))

(test-equal?
 "raízes de x² + 0x + 0 são 0 e 0"
 (raízes 1 0 0) '(0 0))

(test-equal?
 "raízes de x² + 0x - 1 são -1 e 1"
 (raízes 1 0 -1)
 '(-1 1))

(test-equal?
 "raízes de x² + 0x - 4 são -2 e 2"
 (raízes 1 0 -4)
 '(-2 2))

(test-equal?
 "raízes de 2x² + 0x - 2 são -1 e 1"
 (raízes 2 0 -2)
 '(-1 1))

(test-equal?
 "raízes de 2x² + 0x - 2 são -1 e 1"
 (raízes 2 0 -8)
 '(-2 2))

(test-equal?
 "raízes de 1x² -1x - 0 são 0 e 1"
 (raízes 1 -1 0)
 '(0 1))