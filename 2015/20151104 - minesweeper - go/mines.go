package mines

import "strings"
import "strconv"

func FillMines(board string) string {
	var out string
	for i, c := range board {
		switch c {
		case '*':
			out += "*"
		case '.':
			count := strings.Count(board[i-1:i+2], "*")
			out += strconv.Itoa(count)
		}
	}
	return out
}
