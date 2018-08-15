(ns caminho-seguro.core
  (:gen-class))

(defn caminho-seguro
	[caminhos]
	(if (> (count caminhos) 2)
		(reduce + (map (fn [caminho] (last caminho)) caminhos))
		"Pernoite"))