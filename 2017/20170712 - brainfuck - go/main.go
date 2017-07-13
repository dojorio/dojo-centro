package main
import "strings"

int buffer = 0;

func Interpreta(data string) string {
	// 43 => '+'
	if "+" == strings(data[0]) {
		buffer++;
		anotherData := make([]string, len(data) - 1)

		for index, element := range data {
			anotherData[index] = data[index + 1]
		}
		Interpreta(anotherData)
	} 
}
	if data == "." { return "0"}
	return ""
}