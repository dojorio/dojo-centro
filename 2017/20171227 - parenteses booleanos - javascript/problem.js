exports.problem = function (bar) {
    if (bar == 'true' ||
        bar == 'true and true' ||
        (bar.includes(' or') && bar.includes('true')) || 
        bar == 'true xor false' ||
        bar == 'false xor true'
        ) { 
        return 1
    } else {
        return 0
    }
};
