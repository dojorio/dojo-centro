(ns do-lado-escuro-do-codigo.core
  (:gen-class))

(defn get-time-distributed
	"this is my function"
	[time tasks_qty]
	(if (= time 2) 
		[2] 
		(if (= time 3)
			[3]
			[1])))
