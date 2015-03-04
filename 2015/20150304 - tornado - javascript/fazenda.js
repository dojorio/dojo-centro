exports.refazer_cerca = function (cerca) {
    if((cerca[1] === 0 && cerca[2] === 0) ||
       (cerca[2] === 0 && cerca[3] === 0) ||
       (cerca[0] === 0 && cerca[1] === 0))
        return 1

    return 0
}