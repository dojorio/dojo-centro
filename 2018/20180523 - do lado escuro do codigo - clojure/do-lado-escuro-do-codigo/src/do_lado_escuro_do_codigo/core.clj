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
		(if (< time 6)
			[(- time 1) 1]
			(if (= time 9)
				[8 1]
				[(- time 2) 2]))))
