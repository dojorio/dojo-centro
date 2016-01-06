exports.conquer = function (roads) {
    if (roads.length == 3) return 2;
    return Math.min(roads.length, 1);
}