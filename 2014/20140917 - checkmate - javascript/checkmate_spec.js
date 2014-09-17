var assert = require('assert'),
    checkmate = require('./checkmate').checkmate

describe('checkmate', function () {
  it("['Wa3'], 'Wa1'", function () {
    assert.equal(checkmate(['Wa3'], 'Wa1'), false)
  })

  it("['Wa3', 'Tc1'], 'Wa1'", function () {
    assert.equal(checkmate(['Wa3', 'Tc1'], 'Wa1'), true)
  })

  it("['Wa4', 'Tc1'], 'Wa1'", function () {
    assert.equal(checkmate(['Wa4', 'Tc1'], 'Wa1'), false)
  })
})