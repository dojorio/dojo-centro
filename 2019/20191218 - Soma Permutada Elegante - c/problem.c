#include <stdio.h>
#include <stdlib.h>


//https://www.urionlinejudge.com.br/judge/pt/problems/view/1055

int compara(int, int);

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
	    } else {
	    	soma = 0;
	    	qsort(n, list, sizeof(int), &compara);
	   
	   		for(int i=0; i<list;i++){
	   			int elementoAtual = n[i];
	   			for(int j=i+1;j<list;j++){


	   			}

	   		}
	    	for(int i = 0; i< list/2;i++){
	    		soma += abs(n[i] - n[list - (i + 1)]);
	    		soma += abs(n[i] - n[list - (i + 2)]);
	    	}
	    }

	    printf("%d\n", soma);
    }

	return 0;

}

int compara(int a, int b) {
    return a - b;
}