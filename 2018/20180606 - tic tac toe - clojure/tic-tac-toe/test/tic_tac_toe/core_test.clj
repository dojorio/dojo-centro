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