(ns do-lado-escuro-do-codigo.core-test
  (:require [clojure.test :refer :all]
            [do-lado-escuro-do-codigo.core :refer :all]))


(deftest a-test
  (testing "one minute, one task"
    (is (= (get-time-distributed 1 1) [1]))))

(deftest b-test
  (testing "two minutes, one task"
    (is (= (get-time-distributed 2 1) [2]))))

(deftest c-test
  (testing "three minutes, one task"
    (is (= (get-time-distributed 3 1) [3]))))

(deftest d-test
  (testing "two minutes, two tasks"
    (is (= (get-time-distributed 2 2) [1 1]))))

(deftest e-test
  (testing "three minutes, two tasks"
    (is (= (get-time-distributed 3 2) [2 1]))))

(deftest f-test
  (testing "four minutes, two tasks"
    (is (= (get-time-distributed 4 2) [3 1]))))
