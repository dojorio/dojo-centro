#include <stdio.h>
#include <stdlib.h>

int main() {
	int cases;
	int list;
	int n[4];
	int soma;

    scanf("%d", &cases);

    for (; cases > 0; cases--) {
    	scanf("%d", &list);

    	for (int i = 0; i < list; i++) {
    		scanf("%d", n + i);
    	}

    	if (list == 2) {
	    	soma = abs(n[1] - n[0]);
	    } else if (list == 3){
	    	soma = abs(n[0] - n[1]) + abs(n[0] - n[2]) + abs(n[1] - n[2]);
	    } else {
	    	soma = 2;
	    }

	    printf("%d\n", soma);
    }

	return 0;

}