var assert = require('assert'),
    miojo = require('./problem').problem;

describe('Miojo', function() {
    it('duas ampulhetas pares diferentes', function () {
        var amp1 = 4
        var amp2 = 2 
        assert.equal(miojo(amp1, amp2), false)
    })

    it('ampulhetas 1 e 2', function () {
        var amp1 = 1
        var amp2 = 2 
        assert.equal(miojo(amp1, amp2), 3)
    })

	it('ampulhetas 1 e 4', function () {
        var amp1 = 1
        var amp2 = 4 
        assert.equal(miojo(amp1, amp2), 3)
    })

})