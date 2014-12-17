exports.isValidDate = function(dateStr) {
  var months = [
    'Aligator',
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

  var Alligator = ["0","13", "26"];
  var Bog = ["1", "14"];
  
  var date = dateStr.split('-');
  var day = date[0];
  var month = date[1];
  var year = date[2];

  if (month == 'Alligator' && Alligator.indexOf(day) != -1) {
    return true;
  }

  if (month == 'Bog' && day % 13 == months.indexOf("Bog")) {
    return true;
  }

  return false;
}