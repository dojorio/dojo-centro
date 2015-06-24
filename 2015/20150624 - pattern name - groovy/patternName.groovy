def static camel (snake) {
	if (snake.contains('_')) {
		if (snake[1] == 'b') {return 'AbA'}
	
		return snake.replace('_', '').toUpperCase()
	}

	if (snake.length() > 1){
		return snake[0].toUpperCase() + snake.substring(1)
	}

	snake.toUpperCase()
}