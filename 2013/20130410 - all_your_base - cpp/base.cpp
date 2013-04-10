#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main() {
	int caso = 0, casos;
	string simbolos;
	cin >> casos;

	while(caso++ < casos) {
		int total = 0;
		cin >> simbolos;
		for(int i = 0; i < simbolos.size(); i++){
			total += 1*(pow(2,i));
		}

		cout << "Case #" << caso << ": " << total << endl;
	}
}
