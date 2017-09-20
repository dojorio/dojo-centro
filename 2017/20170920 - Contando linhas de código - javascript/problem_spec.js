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

    it('simple class three lines', function () {
        var fileContent = "public class Teste {println('');\nprintln('');\n}"
        assert.equal(countCode(fileContent), 3)
    })
  
    it('simple class three lines, one empty', function () {
        var fileContent = "public class Teste {println('');\n\nprintln('');\n}"
        assert.equal(countCode(fileContent), 3)
    })

    it('simple class three lines, one trinable line', function () {
    	var fileContent = "public class Teste {println('');\n   \nprintln('');\n}"
    	assert.equal(countCode(fileContent), 3)
    })

    it('simple class three lines, simple comment', function () {
    	var fileContent = "public class Teste {println('');\n//jose\nprintln('');\n }"
    	assert.equal(countCode(fileContent), 3)
    })

    it('simple class three lines, space + simple comment ', function () {
    	var fileContent = "public class Teste {println('');\n   //jose\nprintln('');\n}"
    	assert.equal(countCode(fileContent), 3)
    })

    it('simple class three lines, complex comment ', function () {
    	var fileContent = "public class Teste {println('');\n   /*jose*/  \nprintln('');\n}"
    	assert.equal(countCode(fileContent), 3)
    })

    it('simple class three lines, more complex comment ', function () {
    	var fileContent = "public class Teste {println('');\n   /*jose*/ println('');  \nprintln('');\n}"
    	assert.equal(countCode(fileContent), 4)
    })

    it('simple class three lines, even more complex comment ', function () {
    	var fileContent = "public class Teste {println('');\n   /*jo\nse*/  \nprintln('');\n}"
    	assert.equal(countCode(fileContent), 3)
    })
})