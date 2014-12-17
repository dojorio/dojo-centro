// http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=828

var assert = require('assert'),
    isValidDate = require('./calendar').isValidDate;

describe('Calendar', function() {
  context('isValidDate', function() {
    it('0-Alligator-0', function() {
      assert.equal(isValidDate('0-Alligator-0'), true);
    });

    it('1-Alligator-0', function() {
      assert.equal(isValidDate('1-Alligator-0'), true);
    });

    it('13-Alligator-0', function() {
      assert.equal(isValidDate('13-Alligator-0'), true);
    });

    it('26-Alligator-0', function() {
      assert.equal(isValidDate('26-Alligator-0'), true);
    });

    it('1-Bog-0', function() {
      assert.equal(isValidDate('1-Bog-0'), true);
    });

    it('28-Damp-0', function() {
      assert.equal(isValidDate('28-Damp-0'), false);
    });

    it('1-Newt-0', function() {
      assert.equal(isValidDate('1-Newt-0'), false);
    });

    it('0-Newt-0', function() {
      assert.equal(isValidDate('0-Newt-0'), true);
    });

    it('0-Overflow-0', function() {
      assert.equal(isValidDate('0-Overflow-0'), true);
    });

    it('1-Overflow-0', function() {
      assert.equal(isValidDate('1-Overflow-0'), false);
    });

    it('1-Overflow-5', function() {
      assert.equal(isValidDate('1-Overflow-5'), true);
    });
  });
  
});