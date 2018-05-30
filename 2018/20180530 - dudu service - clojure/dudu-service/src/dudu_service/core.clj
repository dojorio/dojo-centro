(ns dudu-service.core
  (:gen-class))

(defn dudu-service
	[number-of-documents dependecies]
	(if (= (count (distinct dependecies)) 1)
		"NAO"
		(if (reduce (fn
					 [acc, item]
					 	(and acc (contains? dependecies (reverse item)))
					) dependecies)
			"SIM"	
			"NAO")))