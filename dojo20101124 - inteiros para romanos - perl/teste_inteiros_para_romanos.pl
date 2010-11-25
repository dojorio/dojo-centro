#!/usr/bin/perl

use strict;
use warnings;
use Test::More;
use inteiros_para_romanos qw(inteiro_para_romano);

ok( (inteiro_para_romano(-1) eq "erro") , "-1 vira erro");
ok( (inteiro_para_romano(0) eq "erro") , "0 vira erro");
ok( (inteiro_para_romano(1) eq "I") , "1 vira I");
ok( (inteiro_para_romano(2) eq "II") , "2 vira II");
ok( (inteiro_para_romano(3) eq "III") , "3 vira III");
ok( (inteiro_para_romano(4) eq "IV") , "4 vira IV");
ok( (inteiro_para_romano(5) eq "V") , "5 vira V");
ok( (inteiro_para_romano(6) eq "VI") , "6 vira VI");
ok( (inteiro_para_romano(7) eq "VII") , "7 vira VII");
ok( (inteiro_para_romano(8) eq "VIII") , "8 vira VIII");
ok( (inteiro_para_romano(9) eq "IX") , "9 vira IX");
ok( (inteiro_para_romano(10) eq "X") , "10 vira X");

ok( (inteiro_para_romano(11) eq "XI") , "11 vira XI");
ok( (inteiro_para_romano(12) eq "XII") , "12 vira XII");
ok( (inteiro_para_romano(13) eq "XIII") , "13 vira XIII");
ok( (inteiro_para_romano(14) eq "XIV") , "14 vira XIV");
ok( (inteiro_para_romano(15) eq "XV") , "15 vira XV");

ok( (inteiro_para_romano(16) eq "XVI") , "16 vira XVI");
ok( (inteiro_para_romano(17) eq "XVII") , "17 vira XVII");
ok( (inteiro_para_romano(18) eq "XVIII") , "18 vira XVIII");
ok( (inteiro_para_romano(19) eq "XIX") , "19 vira XIX");



ok( (inteiro_para_romano(20) eq "XX") , "20 vira XX");
ok( (inteiro_para_romano(30) eq "XXX") , "30 vira XXX");
ok( (inteiro_para_romano(40) eq "XL") , "40 vira XL");
ok( (inteiro_para_romano(50) eq "L") , "50 vira L");


done_testing();

