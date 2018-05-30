(ns dudu-service.core-test
  (:require [clojure.test :refer :all]
            [dudu-service.core :refer :all]))

(deftest two-documents-one-dependecy
    (is (= (dudu-service 2 [["A" "B"]]) "NAO")))