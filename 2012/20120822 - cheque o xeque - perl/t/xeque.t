use Test::More;
 
use_ok('xeque'); 
can_ok('xeque', qw(verifica) );

ok(xeque::verifica({
        x => 1,
        y => 1,
        t => "peao",
    })
);

ok(!xeque::verifica({
        x => 1,
        y => 0,
        t => "peao",
    })
);

ok(!xeque::verifica({
        x => 0,
        y => 1,
        t => "peao",
    })
);

ok(xeque::verifica({
        x => 1,
        y => 0,
        t => "torre",
    })
);


ok(xeque::verifica({
        x => 0,
        y => 4,
        t => "torre",
    })
);

ok(!xeque::verifica({
        x => 2,
        y => 3,
        t => "torre",
    })    
);

ok(xeque::verifica({
        x => 5,
        y => 5,
        t => "bispo",
    })    
);

ok(!xeque::verifica({
        x => 3,
        y => 5,
        t => "bispo",
    })    
);

 
 done_testing;
