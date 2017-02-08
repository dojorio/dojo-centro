d = {
	'tesoura' : {
		'lagarto': 'decapita',
		'papel': 'corta',
		'pedra': 'é quebrada pela',
		'spock': 'é derretida pelo',
		'tesoura': 'empata com',
	},
	'papel': {
		'pedra': 'cobre',
		'spock': 'refuta',
		'tesoura': 'é cortado pela',
		'lagarto': 'é comido pelo',
		'papel': 'empata com',
	},
	'pedra':{
		'tesoura': 'quebra',
		'lagarto': 'esmaga',
		'papel': 'é coberta pelo',
		'spock': 'é vaporizada pelo',
		'pedra': 'empata com',
	},
	'lagarto' :{
		'spock': 'envenena',
		'papel': 'come',
		'tesoura': 'é decapitado pela',
		'pedra': 'é esmagado pela',
		'lagarto': 'empata com',
	},
	'spock' : {
		'pedra': 'vaporiza',
		'tesoura': 'derrete',
		'lagarto': 'é envenenado pelo',
		'papel': 'é refutado pelo',
		'spock': 'empata com',
	}
}

def quem_ganha(str1, str2):
	return ' '.join((str1, d[str1][str2], str2))
	