function testeSequencia(i,j){
    maximo = 0;
    for (y=i; y<=j; y++){
        n = y;
        contador = 1;
        while (n != 1) {
            if (n%2 == 0) {
                n = n/2;
            }
            else n = (n*3) + 1;
            contador++;
        }
            if(contador > maximo){
                maximo=contador;
            }
        }
        return  i+" " +j+" "+maximo;
}

