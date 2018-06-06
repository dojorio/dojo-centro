(ns tic-tac-toe.core
  (:gen-class))

(defn tic-tac-toe
	[board]
	(if (= (count board) 0)
		nil
		(let [uniq (distinct (first board))]
			(if (or (> (count uniq) 1) (= (first uniq) "")) 
				(tic-tac-toe (rest board))
				(first uniq)
			))))
