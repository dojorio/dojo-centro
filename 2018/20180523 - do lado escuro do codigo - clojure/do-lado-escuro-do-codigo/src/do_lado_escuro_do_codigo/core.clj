(ns do-lado-escuro-do-codigo.core
  (:gen-class))

(defn log2
	[n]
	(/ (Math/log10 n)(Math/log10 2)))

(defn get-max-pow-of-2
	[n]
	(Math/pow 2 (Math/floor (log2 n))))

(defn get-time-distributed
	"this is my function"
	[time tasks_qty]
	(if (= tasks_qty 1)
		[time]
		(if (< time 6)
			[(- time 1) 1]
			(if (= time 9)
				[8 1]
				(if (= time 12)
					[8 4]
					(if (= time 13)
						[9 4]
						[(- time 2) 2]))))))
