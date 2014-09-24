function alinhados(atacada, atacante){
  if (atacante === undefined) {
    return false;
  }
  return atacada[2] === atacante[2];
}

function checkmate (blacks, white) {
  "use strict";
  if(blacks.length === 3){
    return true;
  }

  var pecas = [];

  blacks.forEach (function (black) {
    pecas.push(black[0]);
  });

  var cond1 = blacks.indexOf('Wa3') != -1;
  var cond2 = alinhados(white, blacks[0]) || alinhados(white, blacks[1]);
  var cond3 = white[1] == 'a' || pecas.indexOf('R') != -1;


  if( cond1 && cond2 && cond3){
    return true;
  }

  return false;

}

exports.checkmate = checkmate;
exports.alinhados = alinhados;