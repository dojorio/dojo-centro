exports.checkmate = function(blacks, white) {

  if(blacks.indexOf('Wa3') != -1 && blacks.indexOf('Tc1') != -1){
    return true;
  }
   
  return false;
}