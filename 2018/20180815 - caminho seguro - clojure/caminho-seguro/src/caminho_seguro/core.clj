(ns caminho-seguro.core
  (:gen-class))


[[1 2 10] [2 3 10] [3 4 20] [4 3 20] [3 1 10]]


(defn caminho-seguro
	[caminhos]
	(if (distinct (map (rest caminhos)))
		()
		(if (> (count caminhos) 2)
		(reduce + (map (fn [caminho] (last caminho)) caminhos))
		"Pernoite")))
	