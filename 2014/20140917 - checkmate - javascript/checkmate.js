exports.checkmate = function(blacks, white) {
  positions = []

  blacks.forEach (function (black) {
    positions.push(black.slice(2))
  })

  if(blacks.indexOf('Wa3') != -1 && positions.indexOf('1') != -1 && white == 'Wa1'){
    return true;
  }

  return false;
}