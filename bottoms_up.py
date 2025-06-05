import unittest
from single_peak import find_bottom

class TestFindBottom(unittest.TestCase):
    def test_single_bottom(self):
        profile = [['a', 'b', 'c'], ['b', 'a', 'c'], ['c', 'b', 'a']]
        remaining = {'a', 'b', 'c'}
        self.assertEqual(find_bottom(profile, remaining), {'a','c'})

    def test_multiple_bottoms(self):
        profile = [['a', 'b', 'c'], ['b', 'c', 'a'], ['c', 'a', 'b']]
        remaining = {'a', 'b', 'c'}
        self.assertEqual(find_bottom(profile, remaining), {'a', 'b', 'c'})

    def test_subset_remaining(self):
        profile = [['c', 'b', 'a'], ['c', 'b', 'a'], ['b', 'c', 'a']]
        remaining = {'b', 'c'}
        self.assertEqual(find_bottom(profile, remaining), {'b','c'})

    def test_single_remaining(self):
        profile = [['a', 'b', 'c'], ['b', 'c', 'a'], ['b', 'c', 'a']]
        remaining = {'b'}
        self.assertEqual(find_bottom(profile, remaining), {'b'})

if __name__ == '__main__':
    unittest.main()
