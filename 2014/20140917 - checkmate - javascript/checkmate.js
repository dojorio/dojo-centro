function alinhados(atacada, atacante){

  return atacada[2] === atacante[2];
}

function checkmate (blacks, white) {


  positions = []
  pecas = [];

  blacks.forEach (function (black) {
    positions.push(black.slice(2))
    pecas.push(black[0])
  })

  cond1 = blacks.indexOf('Wa3') != -1;
  cond2 = alinhados(white, blacks[0]) || alinhados(white, blacks[1]);
  cond3 = white[1] == 'a' || pecas.indexOf('R') != -1;

  if( cond1 && cond2 && cond3){
    return true;
  }

  return false;

}

exports.checkmate = checkmate
exports.alinhados = alinhados