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
	for i, c := range board {
		switch c {
		case '*':
			out += "*"
		case '.':
			start := max(0, i-1)
			end := min(i+2, len(board))
			count := strings.Count(board[start:end], "*")
			out += strconv.Itoa(count)
		}
	}
	return out
}
