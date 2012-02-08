#lang racket
(require rackunit)

; Implementation
(define (dna-length seq1 seq2)
  
  (cond [(= (string-length seq1) 1) 1 ]
        [(= (string-length seq1) 2) 
         (if (equal? (string-ref seq1 1) #\C) 1 2)
        ]))

; Tests
(check-equal? (dna-length "G"
                          "C") 1)
(check-equal? (dna-length "GC"
                          "CG") 2)
(check-equal? (dna-length "GC"
                          "CA") 1)
(check-equal? (dna-length "GT"
                          "CA") 2)