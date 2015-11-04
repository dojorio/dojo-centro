package mines

import "strings"

func FillMines(board string) string {
  return strings.Replace(board, ".", "0", -1)
}