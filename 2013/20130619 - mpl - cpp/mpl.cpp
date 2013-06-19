#include <iostream>
#include <string>
#include <cstring>
using namespace std;

int calcularPassagem(int estacoes) {
    int soma = 0;
    for(int j = 0; j <= estacoes;j++) {
        soma += valorPas - j;
    }
    return soma;
}

int main() {
	int caso = 0, casos;
	cin >> casos;

    
	while(caso++ < casos) {
	
	    int valorPago = 0;
        int valorDevido = 0;
        int totalEstacoes = 0;
	
	    int valorPas, qtd_trajetos;
	    cin >> valorPas >> qtd_trajetos;
	    
	    for(int i=0; i<qtd_trajetos; i++) {
	        int origem, destino, qtd_pessoas;
	        cin >> origem >> destino >> qtd_pessoas;
	        
	        valorDevido += calcularPassagem(destino - origem - 1);
            
	        //valor devido --> quanto deveria pagar
	        for(int j = 0; j < destino - origem;j++) {
	            valorDevido += valorPas - j;
	            totalEstacoes++;
	        }
	    }

        for(int j = 0; j < totalEstacoes;j++) {
            valorPago += valorPas - j;
        }
	    
	    int resultado = valorDevido - valorPago;
	
		cout << "Case #" << caso << ": " << resultado << endl;
	}
}
