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

  if (month == 'Newt')
    return day == 0;
  return day < 28;
}