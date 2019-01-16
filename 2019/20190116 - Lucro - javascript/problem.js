exports.problem = function (cost, receipts) {
	let totalDays = receipts.length
	let totalCost = totalDays * cost
	let totalReceipts = receipts.reduce(add, 0)

	let profit1 = receipts[0] - cost
	let profit2 = receipts[1] - cost

	let profit = totalReceipts - totalCost

	if (profit < profit1) {
		return profit1
	} else if (profit < profit2) {
		return profit2
	}

	return profit >=0 ? profit : 0

	function add(a, b) {
	    return a + b;
	}
};
