(ns tic-tac-toe.core
  (:gen-class))

(defn tic-tac-toe
	[board]
	(if (= (count board) 0)
		nil
		(if (some #{""} (first board))
			nil
			(let [uniq (distinct (first board))]
				(if (> (count uniq) 1)
					(tic-tac-toe (rest board))
					(first uniq)
				)))))
