def static camel (snake) {
			snake.split('_').collect{ 
			it[0].toUpperCase() + it.substring(1) 
		}.join()
	}