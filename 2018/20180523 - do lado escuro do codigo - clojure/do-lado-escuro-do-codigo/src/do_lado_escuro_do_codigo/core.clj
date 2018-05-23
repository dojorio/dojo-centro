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
		[(- time 1) 1]))
