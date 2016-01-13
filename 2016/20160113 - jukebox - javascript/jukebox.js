exports.search = function (playlist) {
    if (Object.keys(playlist).length >= 7){
        return Object.keys(playlist).length + 1;
    }
    return Object.keys(playlist).length;
};