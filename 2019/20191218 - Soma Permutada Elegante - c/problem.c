#include <stdio.h>

int main() {
	int cases;
	int list;
	int n;

    scanf("%d", &cases);

    for (; cases > 0; cases--) {
    	scanf("%d", &list);

    	for (; list > 0; list--) {
    		scanf("%d", &n);
    	}

    	if (n == 1) {
    		printf("0\n");
    	} else {
    		printf("1\n");
    	}
    }

	return 0;

}