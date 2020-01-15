exports.iceBlock = function (blocks, required) {
    if (required == 2) {
        return 2
    }

    if (required == 3) {
        return 3
    }

    return 1
};
