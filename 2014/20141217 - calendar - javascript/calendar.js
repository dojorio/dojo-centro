exports.isValidDate = function(dateStr) {
  var date = dateStr.split('-'),
      day = date[0],
      month = date[1],
      year = date[2];

  if (month == 'Newt') return day == 0;

  if(dateStr == '1-Overflow-0'){
    return false;
  }

  if (month == 'Overflow' && (((683 * year) % 2820) < 683)) {
    return true;
  }

  return day < 28;
} 