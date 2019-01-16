exports.problem = function (cost, receipts) {
	let totalDays = receipts.length
	let totalCost = totalDays * cost
	let totalReceipts = receipts.reduce(add, 0)

	let receipt1 = receipts[0] - cost
	let receipt2 = receipts[1] - cost

	if (totalReceipts < receipt1) {
		return receipt1
	} else if (totalReceipts < receipt2) {
		return receipt2
	}

	let profit = totalReceipts - totalCost
	if (profit >=0) {
		return profit
	}
	else{
		return 0
	}

	function add(a, b) {
	    return a + b;
	}
};
