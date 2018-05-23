(ns do-lado-escuro-do-codigo.core
  (:gen-class))

(defn log2
	[n]
	(/ (Math/log10 n)(Math/log10 2)))

(defn get-max-pow-of-2
	[n]
	(int (Math/pow 2 (Math/floor (log2 n)))))

(defn get-time-distributed
	"this is my function"
	[time tasks_qty]
	(if (= tasks_qty 1)
		[time]
		(let [max-time (get-max-pow-of-2 (- time 1))
			  min-time (max (get-max-pow-of-2 (- time max-time)) 1)
			  remaining-time (- time (+ max-time min-time))]
			  [(+ max-time remaining-time) min-time])))
