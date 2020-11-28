import unittest
from main import wedding_graph


class TestGraph(unittest.TestCase):
    def setUp(self) -> None:
        self.first_list = [(1, 2), (2, 4), (3, 5)]
        self.second_list = [(1, 2), (2, 4), (1, 3), (3, 5), (8, 10)]
        self.third_list = [(4, 2), (6, 8), (4, 10)]  # only women
        self.forth_list = [(4, 2), (2, 1), (2, 3)]  # all people are from one tribe
        self.first_result = 4
        self.second_result = 6
        self.third_result = 0
        self.forth_result = 0

    def test_first_list(self):
        self.assertEqual(wedding_graph(len(self.first_list), self.first_list), self.first_result)

    def test_second_list(self):
        self.assertEqual(wedding_graph(len(self.second_list), self.second_list), self.second_result)

    def test_third_list(self):
        self.assertEqual(wedding_graph(len(self.third_list), self.third_list), self.third_result)

    def test_forth_list(self):
        self.assertEqual(wedding_graph(len(self.forth_list), self.forth_list), self.forth_result)


if __name__ == '__main__':
    unittest.main( )
