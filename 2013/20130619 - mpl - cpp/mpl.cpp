#include <iostream>
#include <string>
#include <cstring>
using namespace std;

int custo_trajeto(int estacoes) {
    int soma = 0;
    for(int j = 0; j < estacoes; j++) {
        soma += 10 - j;
    }
    return soma;
}

int main() {
    int valor_pas, qtd_trajetos;
 	int caso = 0, casos;
	cin >> casos;
    
	while(caso++, cin >> valor_pas >> qtd_trajetos) {
	    int valor_pago = 0;
        int valor_devido = 0;
        int total_estacoes = 0;
	    int max_pessoas=0;
	    
	    for(int i=0; i<qtd_trajetos; i++) {
	        int origem, destino, qtd_pessoas;
	        cin >> origem >> destino >> qtd_pessoas;
	        
	        int tamanho_trajeto = destino - origem;
	        valor_devido += custo_trajeto(tamanho_trajeto) * qtd_pessoas;
            total_estacoes += tamanho_trajeto;
            max_pessoas = max(max_pessoas, qtd_pessoas);
	    }
        
        valor_pago = custo_trajeto(total_estacoes)*max_pessoas;
	    
	    int resultado = valor_devido - valor_pago;
	
		cout << "Case #" << caso << ": " << resultado << endl;
	}
}
