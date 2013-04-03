package main

import "strings"

func ContagemDePossibilidades(expr string) int {
	result := 0
	if expr == "T" {
		result = 1
	} else {
		result = strings.Count(expr, "v")
	}
	return result
}
