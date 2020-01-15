exports.iceBlock = function (blocks, required) {
    blocks.sort((a, b) => b - a)

    return blocks.reduce(function (total, elemento) {
        var division = Math.floor(required / elemento)
        required = required % elemento

        return total + division
    }, 0)
};
