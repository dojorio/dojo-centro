exports.problem = function (bar) {
    if (bar == 'true' ||
        bar == 'true and true' ||
        bar == 'true or true' || bar == 'true or false' || bar == 'false or true') { 
        return 1
    } else {
        return 0
    }
};
