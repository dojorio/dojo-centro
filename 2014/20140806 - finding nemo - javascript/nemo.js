exports.findNemo = function(walls, doors, nemo){
  if (walls.length <= 3) {
    return 0;
  }

  var sum_directions = walls.reduce(function(soFar,wall){
    console.log(soFar, 123)
    return soFar += wall[2];
  });


  if (sum_directions != 2 ) {
    return 0;
  }

  // if(walls[0][1] == walls[3][1]) {
  //   return 0;
  // }

  return doors.length;
}
