exports.iceBlock = function (blocks, required) {
    
    if (blocks.length == 2) {

        return Math.floor(required / blocks[1] )+ required % blocks[1]
        
    }

    return required 
};
