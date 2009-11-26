$(function(){
module("Saving Time");

test("00:00", function() {
    var time = "00:00";
    var relogio = ["x", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11];
    isSet( relogio, show_clock(time), "");
});

test("12:00", function() {
    var time = "12:00";
    var relogio = ["x", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11];
    isSet( relogio, show_clock(time), "");
});

test("01:05", function() {
    var time = "01:05";
    var relogio = [0, "x", 2, 3, 4, 5, 6, 7, 8, 9, 10, 11];
    isSet( relogio, show_clock(time) , "");
});

test("02:10", function() {
    var time = "02:10";
    var relogio = [0, 1, "x", 3, 4, 5, 6, 7, 8, 9, 10, 11];
    isSet( relogio, show_clock(time) , "");
});

test("02:12", function() {
    var time = "02:12";
    var relogio = [0, 1, "x", 3, 4, 5, 6, 7, 8, 9, 10, 11];
    isSet( relogio, show_clock(time) , "");
});

test("02:14", function() {
    var time = "02:14";
    var relogio = [0, 1, "x", 3, 4, 5, 6, 7, 8, 9, 10, 11];
    isSet( relogio, show_clock(time) , "");
});

test("06:00", function() {
    var time = "06:00";
    var relogio = ["m", 1, 2, 3, 4, 5, "h", 7, 8, 9, 10, 11];
    isSet( relogio, show_clock(time) , "");
});

test("14:00", function() {
    var time = "14:00";
    var relogio = ["m", 1, "h", 3, 4, 5, 6, 7, 8, 9, 10, 11];
    isSet( relogio, show_clock(time) , "");
});

test("17:30", function() {
    var time = "17:30";
    var relogio = [0, 1, 2, 3, 4, "h", "m", 7, 8, 9, 10, 11];
    isSet( relogio, show_clock(time) , "");
});

test("19:10", function() {
    var time = "19:10";
    var relogio = [0, 1, "m", 3, 4, 5, 6, "h", 8, 9, 10, 11];
    isSet( relogio, show_clock(time) , "");
});

test("20:49", function() {
    var time = "20:49";
    var relogio = [0, 1, 2, 3, 4, 5, 6, 7, "h", "m", 10, 11];
    isSet( relogio, show_clock(time) , "");
});

});
