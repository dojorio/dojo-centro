
d = {
	'tesoura' : {
		'lagarto': 'decapita',
		'papel': 'corta',
	},
	'papel': {
		'pedra': 'cobre',
		'spock': 'refuta'
	}
}



def quem_ganha(str1, str2):
	if str1 in d:
		return ' '.join((str1, d[str1][str2], str2))
	return ' '.join((str2, d[str2][str1], str1))
