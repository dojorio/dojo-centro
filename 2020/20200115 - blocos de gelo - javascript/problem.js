exports.iceBlock = function (blocks, required) {
    if (blocks.length == 2) {
        if (required > 2 * blocks[1]) {
            return 3
        }

        if (required > blocks[1]) {
            return 2
        }

        return 1
    }

    return required 
};
