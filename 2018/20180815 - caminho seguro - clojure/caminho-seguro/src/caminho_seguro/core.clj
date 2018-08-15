(ns caminho-seguro.core
  (:gen-class))



(defn counter
	[all-elements]
	(let [counter {}]
		(map (fn [[k v]] {k (inc v) }) all-elements)))


(defn caminho-seguro
	[caminhos]
	(let [
		 all-elements (concat (map first caminhos) (map second caminhos ) )
		 non-dupes (distinct all-elements)
	    ]
	(if (distinct (map (rest caminhos)))
		(if (> (count caminhos) 2)
		(reduce + (map (fn [caminho] (last caminho)) caminhos))
		"Pernoite"))))
	
		
		

	