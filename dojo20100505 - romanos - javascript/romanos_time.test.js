$(function(){
module("Romanos");

test("1 > I", function() {

    equals("I", Arabe2Romanos(1),"teste");
});
test("2 > II", function() {

    equals("II", Arabe2Romanos(2),"teste");
});
test("3 > III", function() {

    equals("III", Arabe2Romanos(3),"teste");
});
test("4 > IV", function() {
    equals("IV", Arabe2Romanos(4),"teste");
});
test("5 > V", function() {
    equals("V", Arabe2Romanos(5),"teste");
});
test("7 > VII", function() {
    equals("VII", Arabe2Romanos(7),"teste");
});
test("101 > CI", function() {
    equals("CI", Arabe2Romanos(101),"teste");
});
test("2979 > MMCMLXXIX", function() {
    equals("MMCMLXXIX", Arabe2Romanos(2979),"teste");
});

});
