exports.findNemo = function(walls, doors, nemo){
  if (walls.length < 4) {
    return 0;
  }

  var directions_sum = walls.reduce(function(soFar,wall){
    return soFar += wall[2];
  }, 0);

  // Tenho uma sala de 4 paredes com pelo menos 1 porta
  if (directions_sum == 2 && walls.length == 4 && doors.length > 0) {
    return 1;
  }

  // Não tenho uma sala
  if (directions_sum != 2) {
    return 0;
  }

  return doors.length;
}
