package main

import "strings"

func Interpreta(data string) string {
	if strings.Contains(data, "++."){
		return "2"
	}
	
	if strings.Contains(data, "+.") {
		return "1"
	}

	if strings.Contains(data, ".+") {
		return "0"
	}

	if strings.Contains(data, "."){
		return "0"
	}
		


	return ""
}