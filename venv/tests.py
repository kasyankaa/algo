import unittest
from main import KMPAlgorythm

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.first_text = "abcdacdfsca"
        self.first_pattern = "dac"
        self.first_result = [3,5]
        self.second_text = "ababahalamaha"
        self.second_pattern = "aba"
        self.second_result = [0, 2]
        self.second_result = [2, 4]
        self.third_text = "ASDFGHJKLASDFGHJ"
        self.third_pattern = "ttyu"
        self.third_result = 0




    def test_1(self):
        self.assertEqual(KMPAlgorythm(self.first_pattern, self.first_text), self.first_result)

    def test_2(self):
        self.assertEqual(KMPAlgorythm(self.second_pattern, self.second_text), self.second_result)
    def test_3(self):
        self.assertEqual(KMPAlgorythm(self.third_pattern, self.third_text), self.third_result)

if __name__ == '__main__':
    unittest.main( )