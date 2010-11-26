Clock = function(time) {
    time = time.split(":");
    time[0] = parseInt(time[0]);
    time[1] = parseInt(time[1]);
    this.hora = time[0] % 12;
    this.minuto = Math.floor(time[1] / 5);   
}

function show_clock(time) {
    var clock = new Clock(time);
    var relogio = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11];
    relogio[clock.hora] = "h";
    relogio[clock.minuto] = "m";
    if ( clock.hora == clock.minuto){
        relogio[clock.hora] = "x";
    }
    return relogio;
}