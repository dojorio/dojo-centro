def static camel (snake) {
	if (snake.length() == 2){
		if (snake[0] == 'b') {
			return 'B' + snake[1]
		}

		return 'A' + snake[1]
	}

	snake.toUpperCase()
}