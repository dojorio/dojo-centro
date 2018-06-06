(ns tic-tac-toe.core-test
  (:require [clojure.test :refer :all]
            [tic-tac-toe.core :refer :all]))

; [x o VELHA nil]
(deftest a-test
  (testing "x win"
    (is (= (tic-tac-toe [
    		["x" "x" "x"] 
    		["" "" ""] 
    		["" "" ""]
    	]) "x"))))

(deftest b-test
  (testing "o win"
    (is (= (tic-tac-toe [
    		["o" "o" "o"] 
    		["" "" ""] 
    		["" "" ""]
    	]) "o"))))

(deftest c-test
  (testing "not finished"
    (is (= (tic-tac-toe [
    		["o" "o" ""] 
    		["" "" ""] 
    		["" "" ""]
    	]) nil))))

(deftest d-test
  (testing "not finished"
    (is (= (tic-tac-toe [
    		["x" "o" ""] 
    		["" "" ""] 
    		["" "" ""]
    	]) nil))))

(deftest e-test
  (testing "not finished"
    (is (= (tic-tac-toe [
    		["x" "o" "o"] 
    		["" "" ""] 
    		["" "" ""]
    	]) nil))))

(deftest f-test
  (testing "second row, x wins"
    (is (= (tic-tac-toe [
    		["" "" ""] 
    		["x" "x" "x"] 
    		["" "" ""]
    	]) "x"))))

(deftest g-test
  (testing "one col, x wins"
    (is (= (tic-tac-toe [
    		["x" "" ""] 
    		["x" "" ""]
    		["x" "" ""] 
    	]) "x"))))

(deftest h-test
  (testing "one diagonal, x wins"
    (is (= (tic-tac-toe [
    		["x" "" ""] 
    		["" "x" ""]
    		["" "" "x"] 
    	]) "x"))))