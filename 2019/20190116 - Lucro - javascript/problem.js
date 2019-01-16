exports.problem = function (cost, receipts) {
	let totalDays = receipts.length

	if (totalDays == 1)
    	return receipts[0]
    else if (totalDays == 2)
    	return receipts[0] + receipts[1]
    else if (totalDays == 3)
    	return receipts[0] + receipts[1] + receipts[2]


};
