exports.isValidDate = function (dateStr) {
  Alligador = [0,13];
  if(Alligador.indexOf(dateStr.split('-')[0]) != -1){
    return false;
  }
  return true;
}