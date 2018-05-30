(ns dudu-service.core
  (:gen-class))

(defn dudu-service
	[number-of-documents dependecies]
	(if (and (= (count dependecies) 2)
		     (not= (first dependecies) (last dependecies)))
		"SIM"
		(if (and (= (count dependecies) 3)
		     (not= (count (distinct dependecies)) 1))
			"SIM"
			"NAO")))