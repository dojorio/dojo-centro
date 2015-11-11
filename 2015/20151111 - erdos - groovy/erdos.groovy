static def numbers(articles) {
	
	def result = ["Erdos": 0]
	def authors = articles.X - "Erdos"

	authors.each {
		result[it] = 1
	}

	return  result 

}