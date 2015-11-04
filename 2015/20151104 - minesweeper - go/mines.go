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
			start := i - 1
			i = i + 1 if i == 0
			count := strings.Count(board[i-1:i+2], "*")
			out += strconv.Itoa(count)
		}
	}
	return out
}
