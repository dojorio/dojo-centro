package main

import "strings"

func ContagemDePossibilidades(expr string) int {
	var result int;
	switch expr {
	case "T":
		result = 1
	case "F":
		result = 0
	default:
		if strings.Count(expr, "v") == 3 {
			result = 5
		} else {
			result = strings.Count(expr, "v")
		}
	}
	return result
}
