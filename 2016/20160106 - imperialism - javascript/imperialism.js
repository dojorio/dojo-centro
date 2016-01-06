exports.conquer = function (roads) {
    return roads.reduce(function(memo, elm){
        if(memo.indexOf(elm) != -1){
            memo.push(elm);
        }
        return memo;
    }, []).length
    return Math.min(roads.length, 1);
}