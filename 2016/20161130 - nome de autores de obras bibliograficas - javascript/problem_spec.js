var assert = require ('assert'),
  nomeAutor = require('./problem').nomeAutor;

describe('Nome autor com 1 nome em maiusculas', function() {
  it('MARIA', function () {
    assert.equal(nomeAutor('MARIA'), 'MARIA')
  })
})

describe('Nome autor com 1nome com inicial maiuscula', function() {
  it('Maria', function () {
    assert.equal(nomeAutor('Maria'), 'MARIA')
  })
})