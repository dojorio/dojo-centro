(ns tic-tac-toe.core
  (:gen-class))

(defn tic-tac-toe
	[board]
	(if (some #{""} (first board))
		nil
		(if (= (distinct (ffirst board)) '("x"))
			"x"
			"o")))
