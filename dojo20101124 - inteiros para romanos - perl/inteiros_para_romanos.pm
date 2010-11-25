package inteiros_para_romanos;

use strict;
use warnings;
use Switch;
use Exporter 'import';

our @ISA = qw(Exporter);
our @EXPORT_OK = qw(inteiro_para_romano);

sub ies {
    return "I" x shift;
}

sub xises {
    return "X" x shift;
}

sub inteiro_para_romano {

    my $numero = shift;

    if($numero>0 and $numero<4) {
        return "".ies($numero-0);
    } elsif($numero>4 and $numero<9) {
        return "V".ies($numero-5);
    } elsif($numero>9 and $numero<14) {
        return "X".ies($numero-10);
    } elsif($numero>14 and $numero<19) {
        return "XV".ies($numero-15);
    } elsif($numero>19 and $numero<40) {
        return xises($numero/10);
    }

    switch($numero) {
        case 4 { return "IV"; }
        case 14 { return "XIV"; }
        case 9 { return "IX"; }
        case 19 { return "XIX"; }
        case 40 { return "XL"; }

        case 50 { return "L"; }

    }
    return "erro";
}

return 1;

