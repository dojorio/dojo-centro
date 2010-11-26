function Arabe2Romanos(numero){
    romano = ["M", "CM", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];
    arabico = [1000, 900, 100, 90, 50, 40, 10, 9, 5, 4, 1];
    saida = "";
    valor = 0;
    do {
        if (numero >= arabico [valor]) {
            saida += romano [valor];
            numero -= arabico [valor];}
        else {valor++;}
    }
    while (numero > 0)
    return saida;
}
