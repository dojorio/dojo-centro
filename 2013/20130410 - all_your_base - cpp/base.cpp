#include <iostream>
#include <string>
#include <cstring>
using namespace std;

int valor[256];

int main() {
	int caso = 0, casos;
	string simbolos;
	cin >> casos;

	while(caso++ < casos) {
		int total = 0, base = 1;
		cin >> simbolos;

		memset(valor, -1, sizeof valor);
		valor[simbolos[0]] = 1;

		for(int i = 0; i < simbolos.size(); i++){
			if(valor[simbolos[i]] < 0){
				valor[simbolos[i]] = base;
				base++;
			}
		}

		char simbolo_guardado = simbolos[0];
		int fator = 1;
		for(int i = simbolos.size()-1; i >= 0; i--){
			if(simbolos[i] != simbolo_guardado){
				if(valor[simbolos[i]] < 0){
					valor[simbolos[i]] = ((i == 1) ? 0 : 2);
					simbolo_guardado = simbolos[i];
				}
			}
			total += valor[simbolos[i]]*fator;
			fator *= 2;
		}

		cout << "Case #" << caso << ": " << total << endl;
	}
}
