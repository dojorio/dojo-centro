exports.problem = function (cost, receipts) {
	let dailyProfits = receipts.map(dailyProfit)
	let totalProfit  = dailyProfits.reduce(add, 0)
	let maxProfit    = 0

	for (let i = 0; i < dailyProfits.length; i += 1) {
		let acc = 0

		for(let j = i; j < dailyProfits.length; j+=1 ){
			acc = acc + dailyProfits[j]

			if (acc > maxProfit) {
				maxProfit = acc
			}
		}		
	}

	return Math.max(maxProfit, 0)

	function add(a, b) {
	    return a + b;
	}

	function dailyProfit(dailyReceipt) {
		return dailyReceipt - cost
	}
};
