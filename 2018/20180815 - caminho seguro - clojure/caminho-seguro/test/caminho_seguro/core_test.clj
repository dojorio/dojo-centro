(ns caminho-seguro.core-test
  (:require [clojure.test :refer :all]
            [caminho-seguro.core :refer :all]))

(deftest a-test
  (testing "1 2 999"
    (is (= (caminho-seguro [[1 2 999]]) "Pernoite")))
  (testing "Teste 3 caminhos"
    (is (= (caminho-seguro [[1 2 10] [2 3 10] [3 1 10]]) 30)))
  (testing "Teste 3 caminhos outro"
	(is (= (caminho-seguro [[1 2 10] [2 3 10] [3 1 20]]) 40)))
  (testing "Teste 4 caminhos com Pernoite"
	(is (= (caminho-seguro [[1 2 10] [2 3 10] [3 4 20] [4 3 20] [3 1 10]]) "Pernoite"))))
