var assert = require('assert'),
    fazenda = require('./fazenda');

describe("Fazenda Silverado", function() {
  it("cerca completa nao precisa de poste novo", function() {
    assert.equal(fazenda.refazer_cerca([1,1,1,1,1]), 0)
  })

  it("cerca 10011 precisa de 1 poste novo", function() {
    assert.equal(fazenda.refazer_cerca([1,0,0,1,1]), 1)
  })

  it("cerca 10111 não precisa de poste novo", function() {
    assert.equal(fazenda.refazer_cerca([1,0,1,1,1]), 0)
  })

  it("cerca 11001 precisa de 1 poste novo", function() {
    assert.equal(fazenda.refazer_cerca([1,1,0,0,1]), 1)
  })

  it("cerca 10001 precisa de 1 poste novo", function() {
    assert.equal(fazenda.refazer_cerca([1,0,0,0,1]), 1)
  })

  it("cerca 00101 precisa de 1 poste novo", function() {
    assert.equal(fazenda.refazer_cerca([0,0,1,0,1]), 1)
  })

  it("cerca 11100 precisa de 1 poste novo", function() {
    assert.equal(fazenda.refazer_cerca([1,1,1,0,0]), 1)
  })

  it("cerca 01110 precisa de 1 poste novo", function() {
    assert.equal(fazenda.refazer_cerca([0,1,1,1,0]), 1)
  })

  it("cerca 00001 precisa de 2 postes novos", function() {
    var cerca = [0,0,0,0,1]
    assert.equal(fazenda.refazer_cerca(cerca), 2)
  })

  it("cerca 0 0 0 0 0 1 1 0 0 0 1 1 precisa de 3 postes novos", function() {
    var cerca = [0,0,0,0,0,1,1,0,0,0,1,1]
    assert.equal(fazenda.refazer_cerca(cerca), 3)
  })



})
