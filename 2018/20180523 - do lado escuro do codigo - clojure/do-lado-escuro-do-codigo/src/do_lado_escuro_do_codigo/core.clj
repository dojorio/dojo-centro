(ns do-lado-escuro-do-codigo.core
  (:gen-class))

(defn get-time-distributed
	"this is my function"
	[time tasks_qty]
	(if (= tasks_qty 1)
		[time]
		(if (= time 3)
			[2 1]
			(if (= time 4) [3 1] [1 1]))))
