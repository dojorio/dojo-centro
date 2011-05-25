package fizzbuzz;

sub fizzbuzz {
    
    my $m = shift;
    if ($m % 3 == 0) {
        return 'fizz';
    }
    if ($m % 5 == 0) {
        return 'buzz';
    }
   return $m;
}

1;