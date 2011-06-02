#lang racket
(require rackunit)

(define notas (list 100 50 20 10))
; Notas: 100, 50, 20, 10

(define (atm valor)
  (let ([notas  
               (filter (λ (n) (<= n valor)) 
                       '(100 50 20 10))]) 
    (if (empty? notas) '()
    (list* (first notas) (atm (- valor (first notas)))))))









(test-equal? 
 "sacar 100 deve retornar uma nota de 100" 
 (atm 100) (list 100))

(test-equal? 
 "sacar 50 deve retornar uma nota de 50" 
 (atm 50) (list 50))

(test-equal? 
 "sacar 200 deve retornar duas notas de 100" 
 (atm 200) (list 100 100))

(test-equal? 
 "sacar 300 deve retornar três notas de 100" 
 (atm 300) (list 100 100 100))

(test-equal? 
 "sacar 500 deve retornar cinco notas de 100" 
 (atm 500) (list 100 100 100 100 100))

(test-equal? 
 "sacar 150 deve retornar uma nota de 100 e uma nota de 50" 
 (atm 150) (list 100 50))

(test-equal? 
 "sacar 250 deve retornar duas notas de 100 e uma nota de 50" 
 (atm 250) (list 100 100 50))

(test-equal? 
 "sacar 70 deve retornar uma nota de 50 e uma nota de 20" 
 (atm 70) (list 50 20))

(test-equal? 
 "sacar 30 deve retornar uma nota de 20 e uma nota de 10" 
 (atm 30) (list 20 10))

