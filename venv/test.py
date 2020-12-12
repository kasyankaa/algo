import unittest

from main import fantz


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.first_binary_number = '101101101'
        self.first_number = 5
        self.first_result = 3

        self.second_binary_number = '1111101'
        self.second_number = 5
        self.second_result = 1

        self.third_binary_number = '100111011110100100111110110011100101000111100101110010001100111011110100100111110110011100101000110010110000111100101110010001'
        self.third_number = 7
        self.third_result = 5

        self.forth_binary_number = '1111111111111'
        self.forth_number = 1
        self.forth_result = 13

    def test_1(self):
        self.assertEqual(fantz(self.first_binary_number, self.first_number), self.first_result)
    def test_2(self):
        self.assertEqual((fantz(self.second_binary_number,self.second_number)),self.second_result)
    def test_3(self):
        self.assertEqual(fantz(self.third_binary_number,self.third_number),self.third_result)
    def test_4(self):
        self.assertEqual(fantz(self.forth_binary_number,self.forth_number),self.forth_result)





if __name__ == '__main__':
    unittest.main( )
