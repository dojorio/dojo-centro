
tesoura = {
	'lagarto': 'decapita',
	'papel': 'corta',
}

def quem_ganha(str1, str2):
	if str1 == "pedra":
		return str2
	return ' '.join((str1, tesoura[str2], str2))
