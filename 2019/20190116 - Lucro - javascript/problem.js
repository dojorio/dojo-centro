exports.problem = function (cost, receipts) {
	let totalDays = receipts.length
	let totalCost = totalDays * cost
	let totalReceipts = receipts.reduce(add, 0)
	let dailyProfits  = receipts.map(dailyProfit)

	let totalProfit = totalReceipts - totalCost
	let maxProfit = totalProfit

	for (let i = 0; i < dailyProfits.length; i += 1) {
		if (dailyProfits[i] > totalProfit) {
			maxProfit = dailyProfits[i]
		}
	}

	return maxProfit >= 0 ? maxProfit : 0

	function add(a, b) {
	    return a + b;
	}

	function dailyProfit(dailyReceipt) {
		return dailyReceipt - cost
	}
};
