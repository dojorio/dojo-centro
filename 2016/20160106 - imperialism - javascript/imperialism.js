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
}