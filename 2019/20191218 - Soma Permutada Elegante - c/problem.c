#include <stdio.h>
#include <stdlib.h>

int main() {
	int cases;
	int list;
	int n[3];

    scanf("%d", &cases);

    for (; cases > 0; cases--) {
    	scanf("%d", &list);

    	for (int i = 0; i < list; i++) {
    		scanf("%d", n + i);
    	}

    	if (list == 2) {
	    	if (n[0] == n[1]) {
	    		printf("0\n");
	    	} else {
	    		printf("%d\n", abs(n[1] - n[0]));
	    	}
	    } else {
	    	if (n[0] == n[1] && n[0] == n[2]) {
	    		printf("0\n");
	    	} else {
	    		printf("2\n");
	    	}
	    }
    }

	return 0;

}