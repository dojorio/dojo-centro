package xeque;

sub verifica {
    my $peca = shift;
    if ($peca->{t} eq "peao") {
        if ($peca->{y} == 1 and abs($peca->{x}) == 1) {
            return 1;
        }
    }
    elsif ($peca->{t} eq "torre") {
        if ($peca->{y} == 0 or $peca->{x} == 0) {
            return 1;
        }
    }
    elsif ($peca->{t} eq "bispo") {
        if (abs($peca->{y}) == abs($peca->{x})) {
            return 1;
        }
    }
    return 0;
}

1;
