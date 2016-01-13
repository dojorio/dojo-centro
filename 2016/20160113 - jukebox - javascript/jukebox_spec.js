var assert = require ('assert'),
    jukebox = require('./jukebox');

describe('jukebox', function() {
    it('two songs', function () {
        var playlist = {
            a_flor: 'los_hermanos',
            anna_julia: 'los_hermanos'
        }
        var n = '_flor'.length + 'nna_julia'.length
        assert.equal(jukebox.search(playlist), n )
    })

    it('three songs', function () {
        var playlist = {
            a_flor: 'los_hermanos',
            anna_julia: 'los_hermanos',
            quem_sabe: 'los_hermanos',
        }
        var n = '_flor'.length + 
                'nna_julia'.length +
                'quem_sabe'.length
        assert.equal(jukebox.search(playlist), n )
    })
})