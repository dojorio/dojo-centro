package InteirosParaRomanos;
use strict;
use warnings;

use base 'Exporter';

our @EXPORT = 'romano';


sub romano {
    my $numero = shift;
    my %inteirosParaRomanos = (
        1  => 'I',
        2  => 'II',
        3  => 'III',
        4  => 'IV',
        5  => 'V',
        6  => 'VI',
        10 => 'X',
        11 => 'XI',
        15 => 'XV',
        50 => 'L',
        100 => 'C',
        500 => 'D',
        1000 => 'M',
    );

    my $romano = "";

    for my $casa (1000, 100, 10, 1) {
        my $mcdu = int $numero / $casa;
        if ($mcdu and $mcdu < 4){
            $romano .= $inteirosParaRomanos{$casa} x $mcdu;
            $numero -= $mcdu * $casa;
        } else if ($mcdu == 4) {
            $romano .= $inteirosParaRomanos{$casa} . $inteirosParaRomanos{$casa}
        }
    }

    if ( defined $inteirosParaRomanos{$numero} ) {
        $romano .= $inteirosParaRomanos{$numero};
    }
    return $romano;
}

return 1;

