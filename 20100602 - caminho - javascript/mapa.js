Mapa = function (matriz){

    this.proxima_coordenada = [];

    this.passo = function (x){

//        if (<matriz[1][1] > matriz[1][0] )
//            this.proxima_coordenada = [0,1];
        if (matriz[1][1] > matriz[1][0])
            this.proxima_coordenada = [1,0];
        else
            this.proxima_coordenada = [1,1];
        if (matriz[0][1]< this.proxima_coordenada)
            this.proxima_coordenada = [0,1];



    };
}

