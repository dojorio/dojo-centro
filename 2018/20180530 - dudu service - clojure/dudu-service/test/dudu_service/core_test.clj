;https://www.urionlinejudge.com.br/judge/en/problems/view/1610
(ns dudu-service.core-test
  (:require [clojure.test :refer :all]
            [dudu-service.core :refer :all]))

(deftest two-documents-one-dependecy
    (is (= (dudu-service 2 [[1 2]]) "NAO")))

(deftest two-documents-two-dependecies
    (is (= (dudu-service 2 [[1 2] [2 1]]) "SIM")))

(deftest two-documents-two-repeated-dependecies
    (is (= (dudu-service 2 [[1 2] [1 2]]) "NAO")))

(deftest two-documents-tri-dependecies
    (is (= (dudu-service 2 [[1 2] [2 1] [1 2]]) "SIM")))

(deftest two-documents-tri-repeated-dependecies
    (is (= (dudu-service 2 [[1 2] [1 2] [1 2]]) "NAO")))

(deftest tri-documents-two-dependecies
    (is (= (dudu-service 3 [[1 2] [1 3]]) "NAO")))

(deftest tri-documents-two-dependecies
    (is (= (dudu-service 3 [[1 2] [2 1]]) "SIM")))

