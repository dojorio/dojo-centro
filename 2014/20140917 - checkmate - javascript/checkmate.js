exports.checkmate = function(blacks, white) {

  var king_position = white.slice(1,white.length);
  
  if(king_position[0] )

  if(blacks.indexOf('Wa3') != -1 && blacks.length > 1){
    return true;
  }
   
  return false;
}