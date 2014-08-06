var assert = require('assert')
  findNemo = require('./nemo').findNemo,
  h = 0,
  v = 1;
  
describe('finding nemo',function(){
  it('no walls',function(){
    var walls = [],
      doors = [],
      nemo = [1.5, 1.5];
    assert.equal(findNemo(walls, doors, nemo), 0)
  });

  it('with 4 walls, 1 door and nemo inside',function(){
    var walls = [
        [1, 1, h, 1],
        [1, 1, v, 1],
        [2, 1, v, 1],
        [1, 2, h, 1]
      ],
      doors = [
        [1, 1, v]
      ],
      nemo = [1.5, 1.5];
    assert.equal(findNemo(walls, doors, nemo), 1)
  });

  it('with 3 walls, 1 door and nemo inside',function(){
    var walls = [
        [1, 1, h, 1],
        [1, 1, v, 1],
        [1, 2, h, 1]
      ],
      doors = [
        [1, 1, v]
      ],
      nemo = [1.5, 1.5];
    assert.equal(findNemo(walls, doors, nemo), 0)
  });

  it('with 1 wall, 1 door and nemo',function(){
    var walls = [
        [1, 1, h, 1],
      ],
      doors = [
        [1, 1, h]
      ],
      nemo = [1.5, 1.5];
    assert.equal(findNemo(walls, doors, nemo), 0)
  });

  it('with 4 walls, 1 door and nemo',function(){
    var walls = [
        [1, 1, h, 1],
        [2, 1, h, 1],
        [3, 1, h, 1],
        [4, 1, h, 1]
      ],
      doors = [
        [1, 1, h]
      ],
      nemo = [1.5, 1.5];
    assert.equal(findNemo(walls, doors, nemo), 0)
  });

  it('with 4 walls on the same line, 1 door and nemo',function(){
    var walls = [
        [1, 1, h, 1],
        [2, 1, h, 1],
        [3, 1, h, 1],
        [4, 1, h, 1]
      ],
      doors = [
        [1, 1, h]
      ],
      nemo = [1.5, 1.5];
    assert.equal(findNemo(walls, doors, nemo), 0)
  });

  it('with 4 walls, 1 door and nemo',function(){
    var walls = [
        [1, 1, h, 1],
        [2, 1, h, 1],
        [3, 1, h, 1],
        [4, 2, h, 1]
      ],
      doors = [
        [1, 1, h]
      ],
      nemo = [1.5, 1.5];
    assert.equal(findNemo(walls, doors, nemo), 0)
  });
});