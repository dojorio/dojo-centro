#include <iostream>
#include <string>
#include <cstring>
#define MAX 1000
using namespace std;

int G[MAX][MAX];

int custo_trajeto(int estacoes) {
    int soma = 0;
    for(int j = 0; j < estacoes; j++) {
        soma += 10 - j;
    }
    return soma;
}

int custoG() {
    int soma = 0;
    for(int i=0; i<10; i++) {
        for(int j=0; j<MAX; j++) {
            soma += custo_trajeto(j-i) * G[i][j];
        }
    }
    return soma;
}

int main() {
    int valor_pas, qtd_trajetos;
 	int caso = 0, casos;
	cin >> casos;
    
	while(caso++, cin >> valor_pas >> qtd_trajetos) {
        memset(G, 0, sizeof G);

	    for(int i=0; i<qtd_trajetos; i++) {
	        int origem, destino, qtd_pessoas, tamanho_trajeto;
	        cin >> origem >> destino >> qtd_pessoas;
	        G[origem][destino] = qtd_pessoas;
	    }

        int valor_devido = custoG();
        for(int i=0; i<10; i++) {
            for(int j=i+1; j<10; j++) {
                for(int k=j+1; k<10; k++) {
                    int v = min(G[i][j], G[j][k]);
                    G[i][k] += v;
                    G[i][j] -= v;
                    G[j][k] -= v;
                }
            }
        }
        int valor_pago = custoG();
    
	    int resultado = valor_devido - valor_pago;
	
		cout << "Case #" << caso << ": " << resultado << endl;
	}
}
