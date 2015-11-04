package mines

import "strings"

func FillMines(board string) string {
  if board == "*" {
  	return "*"
  }
  return strings.Replace(board, ".", "0", 0)
}