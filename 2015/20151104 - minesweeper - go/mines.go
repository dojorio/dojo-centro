package mines

import "strings"

func FillMines(board string) string {
	if strings.Contains(board, "*") && strings.Contains(board, ".") {
		return strings.Replace(board, ".", "1", -1)
	}

	return strings.Replace(board, ".", "0", -1)
}
