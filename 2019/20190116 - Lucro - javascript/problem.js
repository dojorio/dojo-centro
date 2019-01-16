exports.problem = function (cost, receipts) {
	let totalDays = receipts.length
	let totalCost = totalDays * cost
	let totalReceipts = receipts.reduce(add, 0)
	let dailyProfits  = receipts.map(dailyProfit)

	let totalProfit = totalReceipts - totalCost
	let maxProfit = 0

	for (let i = 0; i < dailyProfits.length; i += 1) {
		
		let acc = 0
		for(let j = i; j < dailyProfits.length; j+=1 ){
			acc = acc + dailyProfits[j]
			if (acc > maxProfit) {
				maxProfit = acc
			}
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
