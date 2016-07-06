var assert = require ('assert'),
    ocr = require('./problem').ocr;

describe('ocr', function() {
    it('simple sample', function () {
        var bar = ["   ",
                   "   ",
                   "   "]
        assert.equal(ocr(bar), undefined)
    })

    it('one', function () {
        var bar = ["   ",
                   "  |",
                   "  |"]
        assert.equal(ocr(bar), 1)
    })

    it('seven', function () {
        var bar = [" _ ",
                   "  |",
                   "  |"]
        assert.equal(ocr(bar), 7)
    })

    it('four', function () {
        var bar = ["   ",
		           "|_|",
		           "  |"]
        assert.equal(ocr(bar), 4)
    })

    it('nine', function () {
        var bar = [" _ ",
		           "|_|",
		           " _|"]
        assert.equal(ocr(bar), 9)
    })

    it('five', function () {
        var bar = [" _ ",
		           "|_ ",
		           " _|"]
        assert.equal(ocr(bar), 5)
    })

    it('three', function () {
        var bar = [" _ ",
		           " _|",
		           " _|"]
        assert.equal(ocr(bar), 3)
    })

    it('two', function () {
        var bar = [" _ ",
		           " _|",
		           "|_ "]
        assert.equal(ocr(bar), 2)
    })

})