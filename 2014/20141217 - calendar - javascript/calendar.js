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
  var month = months.indexOf(date[1]);
  
  if (parseInt(date[0]) % 13 === month) {
    return true;
  }


  return false;
}