exports.isValidDate = function(dateStr) {
  var date = dateStr.split('-');
  var day = date[0];
  var month = date[1];

  if (month == 'Newt') return day == 0;

  if (month == 'Overflow') return day != 1;

  return day < 28;
}