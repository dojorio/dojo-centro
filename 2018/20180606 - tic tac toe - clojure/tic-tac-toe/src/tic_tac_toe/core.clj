(ns tic-tac-toe.core
  (:gen-class))

(defn tic-tac-toe
	[board]
	(if (some #{""} (first board))
		nil
		(let [
			uniq-1 (distinct (first board))
			uniq-2 (distinct (first board))
			]
			(if (> (count uniq-1) 1)
				(if (> (count uniq-2) 1)
					nil
					(first uniq-2))
				(first uniq-1)))))
