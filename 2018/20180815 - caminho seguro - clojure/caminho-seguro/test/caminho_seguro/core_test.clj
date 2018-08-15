(ns caminho-seguro.core-test
  (:require [clojure.test :refer :all]
            [caminho-seguro.core :refer :all]))

(deftest a-test
  (testing "1 2 999"
    (is (= (caminho-seguro [[1 2 999]]) "Pernoite")))
  (testing "1 2 999"
    (is (= (caminho-seguro [[1 2 10] [2 3 10] [3 1 10]]) 30))))
