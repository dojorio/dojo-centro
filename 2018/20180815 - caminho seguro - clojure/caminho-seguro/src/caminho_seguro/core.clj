(ns caminho-seguro.core
  (:gen-class))

(defn caminho-seguro
	[caminhos]
	(if (> (count caminhos) 2)
		(reduce (fn [acc caminho] (last caminho)) caminhos)
		"Pernoite"))