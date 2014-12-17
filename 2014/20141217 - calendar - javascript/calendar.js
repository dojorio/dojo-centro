exports.isValidDate = function(dateStr) {
  var date = dateStr.split('-'),
      day = date[0],
      month = date[1],
      year = date[2],
      qc;

  if (month == 'Newt') return day == 0;

  if (month == 'Overflow') {
    qc = ((683 * year) % 2820) < 683;
    return qc;
  }

  return day < 28;
}