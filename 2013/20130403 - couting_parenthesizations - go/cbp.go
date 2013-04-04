package main

func max(a, b int) int {
	if a>b {
		return a
	} else {
		return b
	}
}

func ContagemDePossibilidades(expr string) int {
	result := 0;
	switch expr {
	case "T":
		result = 1
	case "F":
		result = 0
	default:
		for i := 1; i < len(expr); i += 2 {
			esquerda := max(ContagemDePossibilidades(expr[:i]), 1)
			direita := max(ContagemDePossibilidades(expr[i+1:]), 1)
			result += direita * esquerda
		}
	}
	return result
}
