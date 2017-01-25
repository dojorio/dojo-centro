
d = {
	'tesoura' : {
		'lagarto': 'decapita',
		'papel': 'corta',
	},
	'papel': {
		'pedra': 'cobre',

	}
}

def quem_ganha(str1, str2):
	return ' '.join((str1, d[str1][str2], str2))
