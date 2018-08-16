(ns caminho-seguro.core
  (:gen-class))



; (defn counter
; 	[all-elements]
; 	(let [counter {}]
; 		(reduce {} (fn [v] {k (inc v) }) all-elements)))


(defn caminho-seguro
	[caminhos]
	(let [
		 all-elements (concat (map first caminhos) (map second caminhos ) )
		 dupe-counts (frequencies all-elements)
	    ]
	(if (> (count (filter (fn [k v] (= v 1)) dupe-counts)) 1)
		(if (> (count caminhos) 2)
			(reduce + (map (fn [caminho] (last caminho)) caminhos))
			"Pernoite"))))
	
		


	