exports.findNemo = function(walls, doors, nemo){
  if (walls.length <= 3) {
    return 0;
  }

  return doors.length;
}


