(ns do-lado-escuro-do-codigo.core-test
  (:require [clojure.test :refer :all]
            [do-lado-escuro-do-codigo.core :refer :all]))


(deftest a-test
  (testing "one minute, one task"
    (is (= (get-time-distributed 1 1) 1)))
  (testing "two minute, one task"
    (is (= (get-time-distributed 2 1) 2))))
