def static lava_jato (total, values) {
	if (values.size() == 1) {
		if(total.abs() == values[0]) {
			return total>0 ? "+" : "-"
		} else {
			return "*"
		}
	}

	if (values.size() == 2) {
		if (total.abs() == values[0] + values[1]) {
			return total > 0 ? "++" : "--"
		} else if (total == values[0] - values[1]) {
			return '+-'
		} else if (total == values[1] - values[0]) {
			return '-+'
		}
	}

	return '*'
}
