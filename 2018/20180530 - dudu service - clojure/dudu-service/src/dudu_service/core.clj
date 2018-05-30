(ns dudu-service.core
  (:gen-class))

(defn dudu-service
	[number-of-documents dependecies]
	(if (= (count (distinct dependecies)) 1)
		"NAO"
		(if (reduce 
				(fn [acc dependecy]
					(or acc (some #{(reverse dependecy)} dependecies))
				)
				false
				dependecies
			)
			"SIM"	
			"NAO")))