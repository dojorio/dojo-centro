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

(deftest g-test
  (testing "five minutes, two tasks"
    (is (= (get-time-distributed 5 2) [4 1]))))

(deftest h-test
  (testing "six minutes, two tasks"
    (is (= (get-time-distributed 6 2) [4 2]))))

(deftest i-test
  (testing "7 minutes, two tasks"
    (is (= (get-time-distributed 7 2) [5 2]))))

(deftest j-test
  (testing "8 minutes, two tasks"
    (is (= (get-time-distributed 8 2) [6 2]))))

(deftest k-test
  (testing "10 minutes, two tasks"
    (is (= (get-time-distributed 10 2) [8 2]))))

(deftest l-test
  (testing "9 minutes, two tasks"
    (is (= (get-time-distributed 9 2) [8 1]))))

(deftest m-test
  (testing "12 minutes, two tasks"
    (is (= (get-time-distributed 12 2) [8 4]))))

(deftest n-test
  (testing "13 minutes, two tasks"
    (is (= (get-time-distributed 13 2) [9 4]))))

(deftest o-test
  (testing "3 minutes, 3 tasks"
    (is (= (get-time-distributed 3 3) [1 1 1]))))