exports.problem = function (cost, receipts) {
	let totalDays = receipts.length
	let totalCost = totalDays * cost
	var sum = receipts.reduce(add, 0);

	function add(a, b) {
	    return a + b;
	}
	return sum - totalCost
};
