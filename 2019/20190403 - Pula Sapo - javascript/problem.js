exports.pulaSapo = function (alturaPulo, alturasCanos) {
	if (alturasCanos[0] == 1 && alturasCanos[1] == 3 ||
		alturasCanos[0] == 2 && alturasCanos[1] == 4 ||
		alturasCanos[0] == 1 && alturasCanos[1] == 4) {
		return 'GAME OVER'
	}

    return 'YOU WIN'
};
