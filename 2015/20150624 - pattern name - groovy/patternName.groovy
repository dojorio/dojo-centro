def static camel (snake) {
	if (snake.length() > 1){
		return snake[0].toUpperCase() + snake.substring(1, snake.length())
	}

	snake.toUpperCase()
}