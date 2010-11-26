import unittest
from espiral import espiral

class TesteEspiral(unittest.TestCase):
    def teste_entra_1_1_sai_1(self):
        self.assertEqual(espiral(1, 1), '1')

    def teste_entra_1_2_sai_1_2(self):
        self.assertEqual(espiral(1, 2), '1 2')

    def teste_entra_1_10_sai_1_ate_10(self):
        self.assertEqual(espiral(1, 10), ' 1  2  3  4  5  6  7  8  9 10')

    def teste_entra_1_100_sai_1_ate_100(self):
        self.assertEqual(espiral(1, 100), '  1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89  90  91  92  93  94  95  96  97  98  99 100')

    def teste_2_e_1(self):
        self.assertEqual(espiral(2, 1), '1\n2')

    def teste_3_e_1(self):
        self.assertEqual(espiral(3, 1), '1\n2\n3')

    def teste_10_e_1(self):
        self.assertEqual(espiral(10, 1), ' 1\n 2\n 3\n 4\n 5\n 6\n 7\n 8\n 9\n10')

    def teste_2_linhas_com_varias_colunas(self):
        self.assertEqual(espiral(2, 2), '1 2\n4 3')

if __name__ == '__main__':
    unittest.main()

