#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int CalcularNaBase2(int n){
	return (pow(2,n));
}

int main() {
	int caso = 0, casos;
	string simbolos;
	cin >> casos;

	while(caso++ < casos) {
		int total = 0;
		int qtdSimbolos = 0;
		char simbolos[];
		cin >> simbolos;
		for(int i = 0; i < simbolos.size(); i++){
			total += CalcularNaBase2(i);
		}

		cout << "Case #" << caso << ": " << total << endl;
	}
}
