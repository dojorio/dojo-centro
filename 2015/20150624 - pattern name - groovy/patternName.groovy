def static camel (snake) {
	if (snake.length() > 1) {
		snake.split('_').collect{ 
			it[0].toUpperCase()
		}.join()
	}

	snake.toUpperCase()
}