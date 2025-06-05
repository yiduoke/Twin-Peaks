import unittest
from single_peak import parse_profile, check_single_peaked

csv_input = '''
e,d,b,c,a
e,d,c,b,a
d,e,c,a,b
'''

profile = parse_profile(csv_input)
result = check_single_peaked(profile)

class TestSinglePeaked(unittest.TestCase):
    def test_single_peaked_from_paper(self):
        csv_input = '''
        e,d,b,c,a
        e,d,c,b,a
        d,e,c,a,b
        '''
        valid_axes = {
            "Axis: a < c < e < d < b",
            "Axis: b < d < e < c < a",
            "Axis: a < c < d < e < b",
            "Axis: b < e < d < c < a"
        }
        profile = parse_profile(csv_input)
        result = check_single_peaked(profile)
        self.assertIn(result, valid_axes)

    def test_single_peaked_from_slide_example(self):
            csv_input = '''
            c,b,d,e,f,a
            a,b,c,d,e,f
            e,f,d,c,b,a
            '''
            valid_axes = {
                "Axis: a < b < c < d < e < f",
                "Axis: f < e < d < c < b < a"
            }
            profile = parse_profile(csv_input)
            result = check_single_peaked(profile)
            self.assertIn(result, valid_axes)
    
    def test_single_peaked_reverse_axis_valid(self):
        csv_input = '''
        b,a,c,d,e
        c,d,b,e,a
        d,e,c,b,a
        '''
        valid_axes = {
            "Axis: a < b < c < d < e",
            "Axis: e < d < c < b < a"
        }
        profile = parse_profile(csv_input)
        result = check_single_peaked(profile)
        self.assertIn(result, valid_axes)

    def test_single_peaked_valid_four_voters(self):
        csv_input = '''
        b,c,a,d
        b,c,d,a
        c,b,a,d
        c,b,d,a
        '''
        valid_axes = {
            "Axis: a < b < c < d",
            "Axis: d < c < b < a",
            "Axis: a < c < b < d",
            "Axis: d < b < c < a"
        }
        profile = parse_profile(csv_input)
        result = check_single_peaked(profile)
        self.assertIn(result, valid_axes)

    def test_single_peaked_all_voters_valid(self):
        csv_input = '''
        b,a,c,d,e
        c,b,d,a,e
        d,e,c,b,a
        e,d,c,b,a
        '''
        valid_axes = {
            "Axis: a < b < c < d < e",
            "Axis: e < d < c < b < a"
        }
        profile = parse_profile(csv_input)
        result = check_single_peaked(profile)
        self.assertIn(result, valid_axes)

if __name__ == '__main__':
    unittest.main()