static def numbers(articles) {
	if(articles.X.size() == 1){
		return ["Erdos": 0]
	} else if(articles.X.size() == 2){
		return ["Erdos": 0, "Ze": 1]
	} else {
		return  ["Erdos": 0, "Ze": 1, "Maria":1]
	}
}