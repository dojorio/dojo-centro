package mines

import "strings"

func FillMines(board string) string {
	if board == "*." {
		return "*1"
	}

	return strings.Replace(board, ".", "0", -1)
}
