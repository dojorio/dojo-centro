var assert = require ('assert'),
  nomeAutor = require('./problem').nomeAutor;

describe('Nome autor com 1 nome em maiusculas', function() {
  it('MARIA', function () {
    assert.equal(nomeAutor('MARIA'), 'MARIA')
  })
})

describe('Nome autor com 1 nome com inicial maiuscula', function() {
  it('Maria', function () {
    assert.equal(nomeAutor('Maria'), 'MARIA')
  })
})


describe('Nome autor com 2 nomes com inicial maiuscula', function() {
  it('Maria Jose', function () {
    assert.equal(nomeAutor('Maria JOSE'), 'JOSE, Maria')
  })
})

describe('Nome autor com 2 nomes com inicial maiuscula', function() {
  it('Maria MERCEDES', function () {
    assert.equal(nomeAutor('Maria MERCEDES'), 'MERCEDES, Maria')
  })
})


describe('Nome autor com 2 nomes com inicial maiuscula', function() {
  it('maria mercedes', function () {
    assert.equal(nomeAutor('maria mercedes'), 'MERCEDES, Maria')
  })
})


describe('Nome autor com 2 nomes com inicial maiuscula', function() {
  it('MARIA MERCEDES', function () {
    assert.equal(nomeAutor('MARIA MERCEDES'), 'MERCEDES, Maria')
  })
})


describe('Nome autor com 3 nomes com inicial maiuscula', function() {
  it('Maria Mercedes Luz', function () {
    assert.equal(nomeAutor('Maria Mercedes Luz'), 'LUZ, Maria Mercedes')
  })
})


describe('Nome autor com 3 nomes com inicial maiuscula', function() {
  it('Maria Mercedes da Luz', function () {
    assert.equal(nomeAutor('Maria Mercedes da Luz'), 'LUZ, Maria Mercedes da')
  })
})