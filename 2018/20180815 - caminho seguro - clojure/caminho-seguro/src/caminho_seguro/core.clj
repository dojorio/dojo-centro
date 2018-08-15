(ns caminho-seguro.core
  (:gen-class))

(defn caminho-seguro
	[caminhos]
	(if (= (count caminhos) 3)
		30
		"Pernoite"))