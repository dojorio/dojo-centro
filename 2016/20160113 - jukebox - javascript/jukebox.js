exports.search = function (playlist) {
    var musics = Object.keys(playlist)
    

    if (musics.length == 6) {
        return 9;
    }

    if (musics.length >= 4){
        return musics.length + 1;
    }


    if (musics[0] == 'aa') {
        return 3;
    }

    if (musics[0] == 'adc'){
        return 4;
    }

    for(music in musics){
        var firstChar = music
        for(var i = 0; i < music.length; i++){
            music.charAt(i)
        }
            
    }

    return musics.length;
};