(ns tic-tac-toe.core
  (:gen-class))

(defn tic-tac-toe
	[board]
	(if (= (ffirst board) "x")
		"x"
		(if (contains? "" (first board)) nil "o")))
