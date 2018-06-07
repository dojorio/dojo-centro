(ns tic-tac-toe.core
  (:gen-class))

(defn transpose [m]
    (apply mapv vector m))

(defn ssecond [coll]
	(second (second coll)))

(defn llast [coll]
	(last (last coll)))

(defn diagonal [board]
    [(ffirst board) (ssecond board) (llast board)])

(defn diagonals [board]
    [
  	    (diagonal board)
  		(diagonal (reverse board))
    ])

(defn is-full [board]
    (not (some #{""} (flatten board))))

(defn verify-winner [board]
	(if (= (count board) 0)
		nil
		(let [uniq (distinct (first board))]
			(if (or (> (count uniq) 1) (= (first uniq) "")) 
				(verify-winner (rest board))
				(first uniq)))))

(defn tic-tac-toe [board]
	(let [result (verify-winner board)
		  tresult (verify-winner (transpose board))
		  dresult (verify-winner (diagonals board))]
		  (or result tresult dresult
		  	  (if (is-full board) "VELHA"))))

;(tic-tac-toe (transpose board)) ;nil