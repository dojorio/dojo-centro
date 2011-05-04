# coding: utf-8

especiais = ("onze","doze","treze","quatorze","quinze","dezesseis", "dezessete","dezoito","dezenove")


numeros = (
   ("","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez"),
   ("","dez","vinte","trinta","quarenta","cinquenta","sessenta","setenta","oitenta","noventa"),
   ("","cento")
)

def cheque_por_extenso(valor):
            
    if valor == 100:
        return "cem reais"

    extenso = valor_por_extenso(valor, 0)

    if valor == 1:
        return "%s real" % extenso
 
    return "%s reais" % extenso
    
def valor_por_extenso(valor, casa):
    if valor > 100:
        return "cento e " + valor_por_extenso(valor - 100, casa)
    if 11 <= valor <= 19:
        return "%s" % especiais[valor-11]

    dezena, unidade = divmod(valor, 10)
    
    if (unidade == 0):
        return valor_por_extenso(dezena, casa+1)
    
    if (dezena == 0):
        return numeros[casa][unidade]
        
    return "%s e %s" % (valor_por_extenso(dezena, casa+1), numeros[casa][unidade])
        
        
