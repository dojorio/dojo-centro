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
				(verify-winner (rest board))
				(first uniq)))))

(defn tic-tac-toe
	[board]
	(let [result (verify-winner board)
		  tresult (verify-winner (transpose board))
		  dresult (verify-winner [[(ffirst board) (second (second board)) (last (last board)) ]])]
		   (or result tresult dresult)))

;(tic-tac-toe (transpose board)) ;nil