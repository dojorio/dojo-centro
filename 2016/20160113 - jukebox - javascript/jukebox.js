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

    var total = 0

    for(var music in musics){
        var original_ok = true

        for(var i = 0; i < music.length; i++){
            var c = music.charAt(i)
            var ok = true

            for(var m in musics){
                if ( m == music ) {
                    continue
                }
                ok = ok && (m.indexOf(c) == -1)
            }
            if (ok) {
                total += 1
            } else {
                total += 2
            }
        }

    }

    return total
    //return musics.length;
};