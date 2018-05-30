(ns dudu-service.core
  (:gen-class))

(defn dudu-service
	[number-of-documents dependecies]
	(if (and (= (count dependecies) 2)
		     (= (first dependecies) (last dependecies)))
		"SIM"
		"NAO"))