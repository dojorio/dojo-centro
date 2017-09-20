var assert = require ('assert'),
    countCode = require('./problem').countCode;

describe('problem', function() {
    it('empty file', function () {
        var fileContent = ""
        assert.equal(countCode(fileContent), 0)
    })

    it('simple class', function () {
        var fileContent = "public class Teste {}"
        assert.equal(countCode(fileContent), 1)
    })

    it('simple class two lines', function () {
        var fileContent = "public class Teste {\n}"
        assert.equal(countCode(fileContent), 2)
    })

    it('simple class two lines', function () {
        var fileContent = "public class Teste {println('');\nprintln('');\n}"
        assert.equal(countCode(fileContent), 3)
    })
})