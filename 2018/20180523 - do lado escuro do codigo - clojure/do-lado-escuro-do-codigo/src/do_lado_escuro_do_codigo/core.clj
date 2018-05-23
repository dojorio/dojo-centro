(ns do-lado-escuro-do-codigo.core
  (:gen-class))

; (defn get-mutiple-2
; 	[n]
; 	(let [acc []
; 		  my-number n]
; 		(reduce acc (fn [n] ()))
; 		))

(defn get-time-distributed
	"this is my function"
	[time tasks_qty]
	(if (= tasks_qty 1)
		[time]
		(if (= time 6)
			[4 2]
			(if (= time 7)
				[5 2]
				(if (= time 8) [6 2] [(- time 1) 1])))))
