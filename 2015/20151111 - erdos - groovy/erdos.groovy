static def numbers(articles) {
	
	def result = ["Erdos": 0]

	if(articles.X.size() == 2){
		def nome = articles.X[1]
		result[nome] = 1

	} else if(articles.X.size() == 3){
		result[articles.X[1]] = 1
		result[articles.X[2]] = 
		
	}

	return  result 

}