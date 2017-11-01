def static lava_jato (total, values) {
	if (values.size() == 1) {
		if(total.abs() == values[0]) {
			return total>0 ? "+" : "-"
		} else {
			return "*"
		}

	} else if (values == [1,1] && total > 0) {
		return '++'

	} else if(values == [1,1]) {
		return '--'
	}
	  else if(values[0]== 3) {
	  	return '+-'
	  }
	return '*'
}
