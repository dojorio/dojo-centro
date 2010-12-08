package espiral;
use Moose;

has estrutura => (is => "rw", isa => "ArrayRef");

sub BUILDARGS {
    my ($class, $x,$y) = @_;
    my $estrutura = _cria_estrutura($x, $y);

    { estrutura => $estrutura };
}

sub _cria_estrutura {
    my ($x, $y) = @_;
    my $struct = [];

    my $count;
    for my $i(0 .. $y) {
       $struct->[$i] = ++$count;
    }
    $struct;
    #for(0 .. $x) {
    #   $struct->[$_] = ++$count;
    #}

    #return [1..$y];

    #if ($y == 2) {
    #    return [ [1, 2] ];
    #}
    #else {
    #    return [ [1] ];
    #}
}


return 1;

