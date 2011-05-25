 use Test::More;
 
 use_ok('fizzbuzz');
 can_ok('fizzbuzz', qw(fizzbuzz) );
 
 my @numbers = qw( 1 2 4 7 8 );
 foreach my $num ( @numbers ) {
 is( fizzbuzz::fizzbuzz( $num ), $num, 
    "fizzbuzz returns same number for $num" );
 }
 
 foreach my $i (1..10) {
    is( fizzbuzz::fizzbuzz( 3 * $i * (int (rand 1000) + 1) ), "fizz",
        'fizzbuzz returns fizz for multiples of 3' );
}
foreach my $i (1..10) {
    is( fizzbuzz::fizzbuzz( 5 * $i * (int (rand 1000) + 1) ), "buzz",
        'fizzbuzz returns buzz for multiples of 5' );
}

 
 
 
 
 done_testing;