exports.isValidDate = function(dateStr) {
  var months = [
    'Alligator',
    'Bog',
    'Crayfish', 
    'Damp', 
    'Eel', 
    'Fen',
    'Gumbo', 
    'Hurricane', 
    'Inundation', 
    'Jaguar', 
    'Kudzu', 
    'Lake', 
    'Marsh'
  ];

  var date = dateStr.split('-');
  var day = date[0];
  var month = date[1];

  /*if (day % 13 == months.indexOf(month)) {
    return true;
  }*/
  if (months[day % 13] == month) {
    return true;
  }

  return false;
}