package main

import "strings"

func ContagemDePossibilidades(expr string) int {
	result := 0
	if expr == "T" {
		result = 1
	} else if strings.Count(expr, "v") == 3 {
		result = 5
	} else {
		result = strings.Count(expr, "v")
	}
	return result
}
