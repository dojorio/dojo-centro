exports.pulaSapo = function (alturaPulo, alturasCanos) {
	if (alturasCanos[1] > alturasCanos[0] + alturaPulo ||
		(alturasCanos.length == 3 
		&& alturasCanos[2] > alturasCanos[1] + alturaPulo )) {
		return 'GAME OVER'
	}

    return 'YOU WIN'
};
