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
})