exports.isValidDate = function(dateStr) {
  Alligator = ["0","13", "26"];
  if (Alligator.indexOf(dateStr.split('-')[0]) != -1) {
    return true;
  }
  return false;
}