exports.iceBlock = function (blocks, required) {
        var total = 0

        blocks.sort((a, b) => b - a)
        for(var i = blocks.length - 1; i>=0; i--){

            var elemento = blocks[i]
            total += Math.floor(required / elemento )
            required = required % elemento

        }
        return total
      
};
