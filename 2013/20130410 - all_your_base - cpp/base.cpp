#include <iostream>
#include <string>
using namespace std;

int valor[256];

int main() {
	int caso = 0, casos;
	string simbolos;
	cin >> casos;

	while(caso++ < casos) {
		int total = 0;
		cin >> simbolos;

		valor[simbolos[0]] = 1;

		int fator = 1;
		for(int i = simbolos.size()-1; i >= 0; i--){
			if(simbolos[i] != simbolos[0]){
				valor[simbolos[i]] = 0;
			}
			total += valor[simbolos[i]]*fator;
			fator *= 2;
		}

		cout << "Case #" << caso << ": " << total << endl;
	}
}
