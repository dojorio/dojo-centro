(ns do-lado-escuro-do-codigo.core
  (:gen-class))

(defn log2
	[n]
	(/ (Math/log10 n)(Math/log10 2)))

(defn get-max-pow-of-2
	[n]
	(int (Math/pow 2 (Math/floor (log2 n)))))

(defn foo
	[time-remaining tarefa-reduzida-menos-1]
	(sum ))

(defn get-time-distributed
	"this is my function"
	[time tasks_qty]
	(if (= tasks_qty 1)
		[time]
		(if (= tasks_qty 2)
			(let [max-pow (get-max-pow-of-2 time)
				  max-time (get-max-pow-of-2 (- time 1))
				  min-time (get-max-pow-of-2 (max (min (- time max-time) (- max-time 1)) 1))
				  remaining-time (- time (+ max-time min-time))]
				  [(+ max-time remaining-time) min-time])
			(if (= time 3)
				[1 1 1]
				(if (= time 4)
					[2 1 1]
					(if (= time 5)
						[3 1 1]
						[4 1 1]))))))
