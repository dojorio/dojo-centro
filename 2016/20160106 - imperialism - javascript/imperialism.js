exports.conquer = function (roads) {
    var test = roads.reduce(function(memo, elm){
        if(memo.indexOf(elm) === -1){
            memo.push(elm);
        }
        return memo;
    }, []).length

    if (test == roads.length){
        return test-2 
    }
    return Math.min(roads.length, 1);
}