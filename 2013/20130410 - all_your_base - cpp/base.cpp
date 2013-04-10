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

		if (simbolos[0] == 'a') {
			valor['b'] = 0;
		} else {
			valor['a'] = 0;
		}

		valor[simbolos[0]] = 1;

		int fator = 1;
		for(int i = simbolos.size()-1; i >= 0; i--){
			total += valor[simbolos[i]]*fator;
			fator *= 2;
		}

		cout << "Case #" << caso << ": " << total << endl;
	}
}
