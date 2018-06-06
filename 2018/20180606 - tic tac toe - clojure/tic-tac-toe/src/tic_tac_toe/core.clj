(ns tic-tac-toe.core
  (:gen-class))

(defn tic-tac-toe
	[board]
	(if (some #{""} (first board))
		nil
		(if (= (ffirst board) "x")
			"x"
			"o")))
