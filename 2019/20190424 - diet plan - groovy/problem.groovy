def static problem (input) {
	diet,breakfeast,lunch=input
	if(breakfeast != "") 
		return ""
	if(lunch == "B") 
	return ""
	return diet.split('').sort().join()
}
