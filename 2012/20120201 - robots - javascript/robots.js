
function comanda(entra, comando){
    var pontos_cardiais = 'SENW';
    
    if(comando == 'M'){        
        y = entra[1] + (entra[2] =="N"? 1 : -1); 
        return [1, y, entra[2]];
    }
    else{
        var sentido = (pontos_cardiais.indexOf(entra[2]) + (comando == "R"? -1: 1))%4;
        
       entra[2] = pontos_cardiais[sentido];
    }
   
   return entra; 
}

