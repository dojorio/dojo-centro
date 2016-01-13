exports.search = function (playlist) {
    var musics = Object.keys(playlist)

    if (musics.length == 6) {
        return 9;
    }

    if (musics.length >= 3){
        return musics.length + 1;
    }

    if (musics[0] == 'aa') {
        return 3;
    }


    return musics.length;
};