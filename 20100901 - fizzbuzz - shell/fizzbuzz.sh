#! /bin/bash
# file: examples/equality_test.sh

eh_divisivel(){
    echo $[ $1 % $2 ] -eq 0
}

eh_divisivel_por_3(){
    eh_divisivel $1 3
}

eh_divisivel_por_5(){
    eh_divisivel $1 5
}

fizzbuzz(){
    if test $(eh_divisivel_por_3 $1)
    then
        echo fizz
    elif test $(eh_divisivel_por_5 $1)
    then
        echo buzz
    else
        echo $1
    fi

}


test_deve_retornar_1_ao_receber_1(){
  assertEquals 1 $(fizzbuzz 1)
}

test_deve_retornar_2_ao_receber_2(){
  assertEquals 2 $(fizzbuzz 2)
}

test_deve_retornar_fizz_ao_receber_3(){
  assertEquals fizz $(fizzbuzz 3)
}

test_deve_retornar_buzz_ao_receber_5(){
  assertEquals buzz $(fizzbuzz 5)
}

test_deve_retornar_fizz_ao_receber_6(){
  assertEquals fizz $(fizzbuzz 6)
}

test_deve_retornar_fizz_ao_receber_9(){
  assertEquals fizz $(fizzbuzz 9)
}

test_deve_retornar_buzz_ao_receber_10(){
  assertEquals buzz $(fizzbuzz 10)
}

test_deve_retornar_fizzbuzz_ao_receber_15(){
  assertEquals fizzbuzz $(fizzbuzz 15)
}

# load shunit2
. ~/bin/shunit2

