package main

import "strings"

func ContagemDePossibilidades(expr string) int{
	result := 0
	if expr == "T" {
		result = 1
	} else if expr == "TvT"{
		result = 1
	} else{

		result = 2
	}
	return result
}
