import unittest
from antivirus import norton

class TestAntivirus(unittest.TestCase):
    def test_empty_file(self):
        input_file = ''
        viruses = ['a', 'aa']
        self.assertEqual(norton(input_file, viruses), [])
    
    def test_one_virus(self):
        input_file = 'a'
        viruses = ['a']
        self.assertEqual(norton(input_file, viruses), ['a'])

    def test_clean_file(self):
        input_file = 'b'
        viruses = ['a']
        self.assertEqual(norton(input_file, viruses), [])

if __name__ == '__main__':
    unittest.main()
