package mines

import "strings"
import "strconv"

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func FillMines(board string) string {
	var out string
	for i, c := range board[1:len(board)] {
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
