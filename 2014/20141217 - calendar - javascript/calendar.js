exports.isValidDate = function(dateStr) {
  var Alligator = ["0","13", "26"];
  var Bog = ["1", "14"];
  
  var date = dateStr.split('-');
  if (date[1] == 'Alligator' && Alligator.indexOf(date[0]) != -1) {
    return true;
  }

  if (date[1] == 'Bog' && Bog.indexOf(date[0]) != -1) {
    return true;
  }

  return false;
}