#!/usr/bin/python3
"""
Unittest module provide utility to tes for individual units of
source code

"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ TestCase for the max_integer function. """

    def test_regular(self):
        """ List of ints(all): should return the max result """
        l = [1, 2, 3, 4, 5]
        result = max_integer(l)
        self.assertEqual(result, 5)

    def test_not_int(self):
        """
        List of non-ints and ints: should raise a TypeError exception

        """
        l = ["RE", 4, "W"]
        self.assertRaises(TypeError, max_integer, l)

    def test_empty(self):
        """ Empty list: should return None """
        l = []
        result = max_integer(l)
        self.assertEqual(result, None)

    def test_negative(self):
        """ List of negative values: should return the max """
        l = [-9, -12, -100]
        result = max_integer(l)
        self.assertEqual(result, -9)

    def test_float(self):
        """ List of mixed ints and floats: should return the max """
        l = [20, 5, 21.2]
        result = max_integer(l)
        self.assertEqual(result, 21.2)

    def test_not_list(self):
        """ Non list argument: should raise a TypeError """
        self.assertRaises(TypeError, max_integer, 7)

    def test_unique(self):
        """ List of one arg - int: should return the value of this int """
        l = [102]
        result = max_integer(l)
        self.assertEqual(result, 102)

    def test_identical(self):
       """Test with a list of identical values: should return the value"""
       l = [2, 2, 2, 2, 2]
       result = max_integer(l)
       self.assertEqual(result, 2)

    def test_strings(self):
        """ List of strings: should return the first string """
        l = ["hi", "hello"]
        result = max_integer(l)
        self.assertEqual(result, "hi")

    def test_none(self):
        """ None as argument: should raise a TypeError """
        self.assertRaises(TypeError, max_integer, None)

if __name__ == '__main__':
    unittest.main()
