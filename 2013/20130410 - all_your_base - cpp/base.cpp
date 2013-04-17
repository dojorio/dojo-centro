#include <iostream>
#include <string>
#include <cstring>
#define ull unsigned long long
using namespace std;

int valor[256];

int main() {
	int caso = 0, casos;
	string simbolos;
	cin >> casos;

	while(caso++ < casos) {
		ull total = 0;
		int base = 0;
		cin >> simbolos;

		memset(valor, -1, sizeof valor);

		for(int i = 0; i < simbolos.size(); i++){
			if(valor[simbolos[i]] < 0){
				valor[simbolos[i]] = base==0?1:
				                     base==1?0:
				                     base;
				base++;
			}
		}
		base = max(base, 2);

		char simbolo_guardado = simbolos[0];
		ull fator = 1;
		for(int i = simbolos.size()-1; i >= 0; i--){
			total += valor[simbolos[i]]*fator;
			fator *= base;
		}

		cout << "Case #" << caso << ": " << total << endl;
	}
}
