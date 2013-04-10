#include <iostream>
using namespace std;


int main() {
	int caso=0, casos;
	cin >> casos;
	int impares[] = {1, 3};
	while(caso++ < casos) {
		cout << "Case #" << caso << ":" << impares[caso];
	}
}
