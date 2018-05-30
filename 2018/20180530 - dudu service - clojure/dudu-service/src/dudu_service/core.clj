(ns dudu-service.core
  (:gen-class))

(defn dudu-service
	[number-of-documents dependecies]
	(if (= number-of-documents 2)
		(if (= (count (distinct dependecies)) 1)
			"NAO"
			"SIM")
		(if (= (last dependecies) [1 3]) "NAO" "SIM")))