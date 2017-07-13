package main

import "strings"

func Interpreta(data string) string {
	if strings.Contains(data, "+.") {
		return "1"
	}

	if strings.Contains(data, ".+") {
		return "0"
	}

	if data == "." { return "0"}
	return ""
}