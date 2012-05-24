#lang racket
(require rackunit)

(define (índice-do-1º-diferente seq)
  2)

((define (rle cAnt seq )
  
  (if
   #;condição  (empty? seq )
                    (not equal? (cAnt) (second seq)))

   #;então    (list (hash 'oque (first seq) 'início 0))
)

#;(define (rle seq)
  
  (if
   #;condição  (and (> (length seq) 1)
                    (equal? (first seq) (second seq)))

   #;então    (list (hash 'oque (first seq) 'início 0))

   #;senão    (for/list ([(elemento i) (in-indexed seq)])
                ( ())
                (hash 'oque elemento 'início i))))


(check-equal? (rle (list 1))
              (list (hash 'oque 1 'início 0)))

(check-equal? (rle (list))
              (list))

(check-equal? (rle (list 0 1))
              (list 
               (hash 'oque 0 'início 0)
               (hash 'oque 1 'início 1)))

(check-equal? (rle (list 0 1 'b))
              (list 
               (hash 'oque 0 'início 0)
               (hash 'oque 1 'início 1)
               (hash 'oque 'b 'início 2)))

(check-equal? (rle (list 0 0))
              (list 
               (hash 'oque 0 'início 0)))

(check-equal? (rle (list 1 1))
              (list 
               (hash 'oque 1 'início 0)))

(check-equal? (rle (list 1 1 1))
              (list 
               (hash 'oque 1 'início 0)))

(check-equal? (índice-do-1º-diferente (list 0 0 7)) 2)

(check-equal? (rle (list 0 0 7))
              (list 
               (hash 'oque 0 'início 0)
               (hash 'oque 7 'início 2)))



(displayln 'ok)