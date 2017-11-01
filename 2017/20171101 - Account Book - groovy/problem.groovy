def static lava_jato (total, values) {
	if (values.size() == 1 || value != -1) {
		if (total < 0  && total == -values[0]) {
		    return '-'
		} else if(total && total == values[0]) {
			return '+'
		}
	} else if (values == [1,1] && total > 0) {
		return '++'

	} else if(values == [1,1]) {
		return '--'
	}

	return '*'
}
