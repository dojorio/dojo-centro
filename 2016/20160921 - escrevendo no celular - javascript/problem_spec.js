var assert = require ('assert'),
    problem = require('./problem').problem;

describe('problem', function() {
    it('vazio', function () {
    	var str = ''
        assert.equal(problem(str), '')
    })
    it('A = 2', function () {
    	var str = 'A'
        assert.equal(problem(str), '2')
    })

    it('B = 22', function () {
    	var str = 'B'
        assert.equal(problem(str), '22')
    })

    it('C = 222', function () {
    	var str = 'C'
        assert.equal(problem(str), '222')
    })

    it('D = 3', function () {
    	var str = 'D'
        assert.equal(problem(str), '3')
    })

    it('AD = 23', function () {
    	var str = 'AD'
        assert.equal(problem(str), '23')
    })

    it('AA = 2_2', function () {
    	var str = 'AA'
        assert.equal(problem(str), '2_2')
    })


    it('AB = 2_22', function () {
    	var str = 'AB'
        assert.equal(problem(str), '2_22')
    })


    it('espaço = 0', function () {
    	var str = ' '
        assert.equal(problem(str), '0')
    })

    it('TESTE DO OTAVIKO!!!!', function () {
    	var str = 'SEMPRE ACESSO O DOJOPUZZLES'
        assert.equal(problem(str), '77773367_7773302_222337777_777766606660366656667889999_9999555337777')
    })
    
})