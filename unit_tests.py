from single_peak import parse_profile, check_single_peaked

csv_input = '''
e,d,b,c,a
e,d,c,b,a
d,e,c,a,b
'''
valid_axes = {
            "Axis: a < c < e < d < b",
            "Axis: a < c < d < e < b"
        }

profile = parse_profile(csv_input)
result = check_single_peaked(profile)
# print("Test Result:", result)

def test_single_peaked_from_paper(self):
    csv_input = '''
    e,d,b,c,a
    e,d,c,b,a
    d,e,c,a,b
    '''
    valid_axes = {
        "Axis: a < c < e < d < b",
        "Axis: a < c < d < e < b"
    }
    profile = parse_profile(csv_input)
    result = check_single_peaked(profile)
    self.assertIn(result, valid_axes)

