use strict;
use warnings;
use Test::More;

use_ok "InteirosParaRomanos";

is romano(1), 'I', 'ao passar 1 deve retornar I';
is romano(2), 'II', 'ao passar 2 deve retornar II';
is romano(3), 'III', 'ao passar 3 deve retornar III';
is romano(4), 'IV', 'ao passar 4 deve retornar IV';
is romano(5), 'V', 'ao passar 5 deve retornar V';
is romano(6), 'VI', 'ao passar 6 deve retornar VI';
is romano(10), 'X', 'ao passar 10 deve retornar X';
is romano(11), 'XI', 'ao passar 11 deve retornar XI';
is romano(15), 'XV', 'ao passar 15 deve retornar XV';
is romano(40), 'XL', 'ao passar 40 deve retornar XL';
is romano(50), 'L', 'ao passar 50 deve retornar L';
is romano(100), 'C', 'ao passar 100 deve retornar C';
is romano(200), 'CC', 'ao passar 200 deve retornar CC';
is romano(300), 'CCC', 'ao passar 300 deve retornar CCC';

is romano(500), 'D', 'ao passar 500 deve retornar D';
is romano(1000), 'M', 'ao passar 1000 deve retornar M';
is romano(2000), 'MM', 'ao passar 2000 deve retornar MM';
is romano(3000), 'MMM', 'ao passar 3000 deve retornar MMM';

done_testing;

