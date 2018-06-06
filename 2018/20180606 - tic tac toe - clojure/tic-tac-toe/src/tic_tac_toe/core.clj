(ns tic-tac-toe.core
  (:gen-class))

(defn transpose [m]
  (apply mapv vector m))

(defn verify-winner
	[board]
	(if (= (count board) 0)
		nil
		(let [uniq (distinct (first board))]
			(if (or (> (count uniq) 1) (= (first uniq) "")) 
				(tic-tac-toe (rest board))
				(first uniq)))))

(defn tic-tac-toe
	[board]
	(let [result (verify-winner board)
		  tresult (verify-winner (transpose board))]
		  (or result tresult)))

;(tic-tac-toe (transpose board)) ;nil