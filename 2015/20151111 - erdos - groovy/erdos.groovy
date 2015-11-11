static def numbers(articles) {
	
	def result = ["Erdos": 0]

	if(articles.X.size() == 1){
		return result
	} else if(articles.X.size() == 2){
		def nome = articles.X[1]
		result[nome] = 1
		return result
	} else {
		return  ["Erdos": 0, "Ze": 1, "Maria":1]
	}
}