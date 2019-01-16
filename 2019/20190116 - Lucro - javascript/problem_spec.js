var assert  = require('assert'),
    problem = require('./problem').problem;

// https://www.urionlinejudge.com.br/judge/pt/problems/view/1310

describe('Lucro', function() {
    it('cost 0, receipts [1]', function () {
        var cost = 0
        var receipts = [1]
        assert.equal(problem(cost, receipts), 1)
    })

    it('cost 0, receipts [2]', function () {
        var cost = 0
        var receipts = [2]
        assert.equal(problem(cost, receipts), 2)
    })

    it('cost 0, receipts [3]', function () {
        var cost = 0
        var receipts = [3]
        assert.equal(problem(cost, receipts), 3)
    })

    it('cost 0, receipts [1, 2]', function () {
        var cost = 0
        var receipts = [1, 2]
        assert.equal(problem(cost, receipts), 3)
    })

    it('cost 0, receipts [1, 2, 3]', function () {
        var cost = 0
        var receipts = [1, 2, 3]
        assert.equal(problem(cost, receipts), 6)
    })

    it('cost 0, receipts [1, 2, 3, 4]', function () {
        var cost = 0
        var receipts = [1, 2, 3, 4]
        assert.equal(problem(cost, receipts), 10)
    })

    it('cost 1, receipts [1, 2, 3, 4]', function () {
        var cost = 1
        var receipts = [1, 2, 3, 4]
        assert.equal(problem(cost, receipts), 6)
    })

    it('cost 2, receipts [1]', function () {
        var cost = 2
        var receipts = [1]
        assert.equal(problem(cost, receipts), 0)
    })

    it('cost 2, receipts [1, 3]', function () {
        var cost = 2
        var receipts = [1, 3]
        assert.equal(problem(cost, receipts), 1)
    })

    it('cost 1, receipts [1, 0, 3]', function () {
        var cost = 1
        var receipts = [1, 0, 3]
        assert.equal(problem(cost, receipts), 2)
    })


})