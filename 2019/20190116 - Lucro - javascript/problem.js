exports.problem = function (cost, receipts) {
	let totalDays = receipts.length
	let totalCost = totalDays * cost
	let totalProfit  = receipts.reduce(add, 0)

	function add(a, b) {
	    return a + b;
	}
	
	let Profit = totalProfit - totalCost
	if (Profit >=0) {
		return Profit
	}
	else{
		return 0
	}
};
