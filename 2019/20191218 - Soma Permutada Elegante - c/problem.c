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
    		if (n[0]<n[1] && n[0]<n[2]) {
    			soma = n[1] - n[0] + n[2] - n[0];
    		} else if (n[1]<n[0] && n[1]<n[2]) {
    			soma = n[0] - n[1] + n[2] - n[1];
    		} else {
    			soma = abs(n[0] - n[2] + n[1] - n[2]);
    		}
	    }else{


	    	
	    }

	    printf("%d\n", soma);
    }

	return 0;

}