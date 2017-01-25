
d = {
	'tesoura' : {
		'lagarto': 'decapita',
		'papel': 'corta',
	},
	'papel': {
		'pedra': 'cobre',
		'spock': 'refuta'
	},
	'pedra':{
		'tesoura': 'quebra',
		'lagarto': 'esmaga'
	},
	'lagarto' :{
		'spock' : 'envenena'
	}
}



def quem_ganha(str1, str2):
	if str1 in d and str2 in d[str1]:
		return ' '.join((str1, d[str1][str2], str2))
	return ' '.join((str2, d[str2][str1], str1))
