var assert = require ('assert'),
    jukebox = require('./jukebox');

describe('jukebox', function() {
    it('two songs', function () {
        var playlist = {
            a_flor: 'los_hermanos',
            anna_julia: 'los_hermanos'
        }
        var n = 'f'.length + 'n'.length
        assert.equal(jukebox.search(playlist), n )
    })

    it('three songs', function () {
        var playlist = {
            a_flor: 'los_hermanos',
            anna_julia: 'los_hermanos',
            quem_sabe: 'los_hermanos',
        }
        var n = 'f'.length + 
                'n'.length +
                'q'.length
        assert.equal(jukebox.search(playlist), n )
    })


    it('three songs with silverchair', function () {
        var playlist = {
            a_flor: 'los_hermanos',
            anna_julia: 'los_hermanos',
            annas_song: 'silverchair',
        }
        var n = 'f'.length + 
                'j'.length +
                's'.length
        assert.equal(jukebox.search(playlist), n )
    })

    it('three songs with silverchair', function () {
        var playlist = {
            a_flor: 'los_hermanos',
            anna_julia: 'los_hermanos',
            annas_song: 'silverchair',
            song_2: 'blur'
        }
        var n = 'f'.length + 
                'j'.length +
                'as'.length +
                '2'.length
        assert.equal(jukebox.search(playlist), n )
    })

    it('five songs with chico_buarque', function () {
        var playlist = {
            a_flor: 'los_hermanos',
            anna_julia: 'los_hermanos',
            annas_song: 'silverchair',
            song_2: 'blur',
            a_banda: 'chico_buarque'
        }
        var n = 'f'.length + 
                'j'.length +
                'as'.length +
                '2'.length +
                'b'.length
        assert.equal(jukebox.search(playlist), n )
    })

    it('five songs with chico_buarque', function () {
        var playlist = {
            a_flor: 'los_hermanos',
            anna_julia: 'los_hermanos',
            annas_song: 'silverchair',
            song_2: 'blur',
            a_banda: 'chico_buarque',
            a_bandana: 'chiclete_com_banana'
        }
        var n = 'f'.length + 
                'j'.length +
                'as'.length +
                '2'.length +
                'b'.length +
                'dan'.length
        assert.equal(jukebox.search(playlist), n)
    })

    it('modesto', function () {
        var playlist = {
            aa: 'a',
            ab: 'b'
        }
        var n = 'aa'.length + 'b'.length
        assert.equal(jukebox.search(playlist), n)
    })
})