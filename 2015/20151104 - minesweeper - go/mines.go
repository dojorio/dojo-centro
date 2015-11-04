package mines

import "strings"
import "strconv"

type Board string

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

func (b Board) FillMines() string {
	var out string
	for i, c := range b {
		switch c {
		case '*':
			out += "*"
		case '.':
			start := max(0, i-1)
			end := min(i+2, len(b))
			count := strings.Count(string(b)[start:end], "*")
			out += strconv.Itoa(count)
		}
	}
	return out
}
