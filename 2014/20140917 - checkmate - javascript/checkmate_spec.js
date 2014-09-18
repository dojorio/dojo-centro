var assert = require('assert'),
    checkmate = require('./checkmate').checkmate,
    alinhados = require('./checkmate').alinhados

describe('alinhados', function () {
  it("'Wa1', 'Wa3'", function () {
    assert.equal(alinhados('Wa3', 'Wa1'), false)
  })

  it("'Wa1', 'Tc1'", function () {
    assert.equal(alinhados('Wa3', 'Wa1'), true)
  })
})

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

  it("['Rd1', 'Wa3'], 'Wh8'", function () {
    assert.equal(checkmate(['Rd1', 'Wa3'], 'Wh8'), false)
  })

  it("['Rd1', 'Wa3'], 'Wb1'", function () {
    assert.equal(checkmate(['Rd1', 'Wa3'], 'Wb1'), true)
  })

  it("['Td1', 'Wa3'], 'Wb1'", function () {
    assert.equal(checkmate(['Td1', 'Wa3'], 'Wb1'), false)
  })
})