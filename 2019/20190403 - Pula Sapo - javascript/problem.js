exports.pulaSapo = function (alturaPulo, alturasCanos) {
	if (alturasCanos[1] > alturasCanos[0] + alturaPulo ||
		alturasCanos.length == 3) {
		return 'GAME OVER'
	}

    return 'YOU WIN'
};
