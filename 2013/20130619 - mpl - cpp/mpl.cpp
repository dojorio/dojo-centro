#include <iostream>
#include <string>
#include <cstring>
using namespace std;

int custo_trajeto(int estacoes) {
    int soma = 0;
    for(int j = 0; j <= estacoes;j++) {
        soma += 10 - j;
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
	        
	        int tamanho_trajeto = destino - origem;
	        valorDevido += custo_trajeto(tamanho_trajeto);
            
            totalEstacoes += tamanho_trajeto + 1;
	    }

        for(int j = 0; j < totalEstacoes;j++) {
            valorPago += valorPas - j;
        }
	    
	    int resultado = valorDevido - valorPago;
	
		cout << "Case #" << caso << ": " << resultado << endl;
	}
}
