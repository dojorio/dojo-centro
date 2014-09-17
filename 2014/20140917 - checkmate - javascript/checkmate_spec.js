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

  it("['Tc1', 'Wa3'], 'Wa1'", function () {
    assert.equal(checkmate(['Tc1', 'Wa3'], 'Wa1'), true)
  })

  it("['Tc2', 'Wa3'], 'Wa1'", function () {
    assert.equal(checkmate(['Tc2', 'Wa3'], 'Wa1'), false)
  })

  it("['Rc1', 'Wa3'], 'Wa1'", function () {
    assert.equal(checkmate(['Rc1', 'Wa3'], 'Wa1'), true)
  })

  it("['Rd1', 'Wa3'], 'Wa1'", function () {
    assert.equal(checkmate(['Rd1', 'Wa3'], 'Wa1'), true)
  })
})