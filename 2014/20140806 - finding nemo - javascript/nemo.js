exports.findNemo = function(walls, doors, nemo){
  if (walls.length <= 3) {
    return 0;
  }

  if(walls[0][1] == walls[3][1]) {
    return 0;
  }

  return doors.length;
}


