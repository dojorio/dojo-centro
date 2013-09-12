import unittest
from antivirus import norton

class TestAntivirus(unittest.TestCase):
    def test_empty_file(self):
        input_file = ''
        viruses = ['a', 'aa']
        self.assertEqual([], norton(input_file, viruses))
    
    def test_one_virus(self):
        input_file = 'a'
        viruses = ['a']
        self.assertEqual(['a'], norton(input_file, viruses))

    def test_clean_file(self):
        input_file = 'b'
        viruses = ['a']
        self.assertEqual([], norton(input_file, viruses))

    def test_file_with_second_virus(self):
        input_file = 'a'
        viruses = ['c', 'a']
        self.assertEqual(['a'], norton(input_file, viruses))

    def test_file_with_second_virus_inside(self):
        input_file = 'ab'
        viruses = ['c', 'a']
        self.assertEqual(['a'], norton(input_file, viruses))

    def test_file_with_2_different_virus(self):
        input_file = 'abc'
        viruses = ['a', 'b']
        self.assertEqual(['a', 'b'], norton(input_file, viruses))

    def test_file_with_2_virus_1_found_twice(self):
        input_file = 'aba'
        viruses = ['a', 'b']
        self.assertEqual(['a', 'b', 'a'], norton(input_file, viruses))
  
    def test_file_with_a_2_chars_virus(self):
        input_file = 'aba'
        viruses = ['ab']
        self.assertEqual(['ab'], norton(input_file, viruses))
        
    def test_file_with_2_2_chars_virus(self):
        input_file = 'abc'
        viruses = ['a', 'ab']
        self.assertEqual(['ab'], norton(input_file, viruses))
          
if __name__ == '__main__':
    unittest.main()
