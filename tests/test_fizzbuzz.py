import sys
import unittest
from io import StringIO

from parameterized import parameterized

import src.fizzbuzz as tested_mod


class TestFizzBuzz(unittest.TestCase):
    def __init__(self, *arg, **kwargs):
        self.tested_func = tested_mod.fizz_buzz

        self.orig_stdout = None
        self.test_stdout = StringIO()

        super().__init__(*arg, **kwargs)

    def setUp(self):
        self.orig_stdout = sys.stdout
        sys.stdout = self.test_stdout

    def tearDown(self):
        sys.stdout = self.orig_stdout

    def test_larger_start_num_than_end_num(self):
        start_num = 5
        end_num = 1
        self.tested_func(start_num, end_num)

        result = self.test_stdout.getvalue()
        expected = ""
        self.assertEqual(result, expected)

    def test_1_to_5(self):
        start_num = 1
        end_num = 5
        self.tested_func(start_num, end_num)

        result = self.test_stdout.getvalue()
        expected = "1 \n2 \n3 Fizz\n4 \n5 Buzz\n"
        self.assertEqual(result, expected)

    def test_9_to_16(self):
        start_num = 9
        end_num = 16
        self.tested_func(start_num, end_num)

        result = self.test_stdout.getvalue()
        expected = (
            "09 Fizz\n10 Buzz\n11 \n12 Fizz\n13 \n14 \n"
            "15 FizzBuzz\n16 \n"
        )
        self.assertEqual(result, expected)


class TestGenFizzBuzzStr(unittest.TestCase):
    def __init__(self, *arg, **kwargs):
        self.tested_func = tested_mod.gen_fizzbuzz_str

        super().__init__(*arg, **kwargs)

    @parameterized.expand([
        [1],
        [2],
        [7],
        [11],
    ])
    def test_non_fizzbuzz(self, num):
        result = self.tested_func(num)
        expected = ""
        self.assertEqual(result, expected)

    @parameterized.expand([
        [3],
        [6],
        [33],
        [33333],
    ])
    def test_fizzes(self, num):
        result = self.tested_func(num)
        expected = "Fizz"
        self.assertEqual(result, expected)

    @parameterized.expand([
        [5],
        [10],
        [55],
    ])
    def test_buzzes(self, num):
        result = self.tested_func(num)
        expected = "Buzz"
        self.assertEqual(result, expected)

    @parameterized.expand([
        [15],
        [15 * 2],
        [15 * 9999],
    ])
    def test_fizzbuzzes(self, num):
        result = self.tested_func(num)
        expected = "FizzBuzz"
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
