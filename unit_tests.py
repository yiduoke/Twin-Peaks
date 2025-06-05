from single_peak import parse_profile, check_single_peaked

csv_input = '''
e,d,b,c,a
e,d,c,b,a
d,e,c,a,b
'''

profile = parse_profile(csv_input)
result = check_single_peaked(profile)
print("Test Result:", result)

