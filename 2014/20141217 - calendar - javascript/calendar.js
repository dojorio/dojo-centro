exports.isValidDate = function(dateStr) {
  Alligator = ["0","13", "26"];
  Bog = ["1"];
  
  date = dateStr.split('-');
  if (Alligator.indexOf(date[0]) != -1) {
    return true;
  }

  if (date[1] == 'Bog' && Bog.indexOf(date[0]) != -1) {
    return true;
  }

  return false;
}