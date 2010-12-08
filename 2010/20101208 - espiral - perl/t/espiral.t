#!/usr/bin/perl
#esses sao mais importantes =) - pragmas!
use strict;
use warnings;

use Test::More;

use_ok("espiral");

ok( my $espiral1x1 = espiral->new(1, 1), "deve criar estrutura da espiral" );

is_deeply($espiral1x1->estrutura, [[1]], "Espiral 1x1.");

 my $espiral1x2 = espiral->new(1,2);
is_deeply( $espiral1x2->estrutura,  [[1, 2]], "Espiral 1x2.");

 my $espiral1x3 = espiral->new(1,3);
is_deeply( $espiral1x3->estrutura,  [[1, 2, 3]], "Espiral 1x3.");

#ok()



done_testing();

