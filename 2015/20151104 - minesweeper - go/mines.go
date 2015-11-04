package mines

import "strings"
import "strconv"

func FillMines(board string) string {
	count := strings.Count(board, "*")
	return strings.Replace(board, ".", strconv.Itoa(count), -1)
}
