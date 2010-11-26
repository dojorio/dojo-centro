public class ConversorInteiroParaRomano
{
	public String converte(int inteiro) 
	{
		String simbolos[] = {"I", "V" ,"X", "L", "C", "D", "M"};
		
		String romano = "";
		String digito_romano;
		int digito;
		int indice = 0;
		if (inteiro >= 4000){
			return null;
		} 
		do {
			digito = inteiro % 10;
			inteiro /= 10;
			digito_romano = "";
			
			if(digito >= 5 && digito <= 8)
			{
				digito_romano += simbolos[indice+1];
				digito -= 5;
			}
			while(digito >= 1 && digito <= 3)
			{
				digito_romano += simbolos[indice];
				digito -= 1;
			}
			if (digito == 4)
			{			
				digito_romano += simbolos[indice]+ simbolos[indice+1];
			}
				
			if(digito == 9)
			{
				digito_romano += simbolos[indice]+simbolos[indice+2];
				
			}
			romano = digito_romano + romano;
			indice += 2;
		} while (inteiro > 0);
		return romano;
	}
}
