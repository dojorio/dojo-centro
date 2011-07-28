def soma(a,b):
	return a+b

def verificaSoma(a,b):
	if a+b > 9:
		return True
	return False
	
def contaDigito(a):	
	numero_de_digitos = len(str(abs(a)))
	return numero_de_digitos
	
def NumeroParaArray(a):
	b = list(str(abs(a)))
	for i,z in enumerate(b):
		b[i] = int(z)
	return b
	
def SomaArray(a,b):
	a_arr = NumeroParaArray(a)
	b_arr = NumeroParaArray(b)
	return a_arr[0]+b_arr[0]
	
	
	