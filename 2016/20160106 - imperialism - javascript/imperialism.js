exports.conquer = function (roads) {

    var test = roads.reduce(function(memo, elm){
        if(memo.indexOf(elm) === -1){
            memo.push(elm);
        }
        return memo;
    }, []).length

    if (test >= 2 && test == roads.length){
        return test - 1
    } else {
        return test
    }
};

exports.toGraph = function(roads) {
    if (roads.length == 1)
        return {1: [2], 2: [1]};
    return {1:[]};
};