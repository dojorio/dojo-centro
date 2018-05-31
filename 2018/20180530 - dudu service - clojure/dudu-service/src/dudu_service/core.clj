(ns dudu-service.core
  (:gen-class))

(defn map-dependencies
	[mapie-dependencies item]
	(merge mapie-dependencies
		   {(first item) [(last item)]}))

(defn dudu-service
	[number-of-documents dependecies]
	(let [complete dependecies]
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
				(reduce fn [dependecies-map] () {} dependecies)))))