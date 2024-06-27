#The dot (.) matches anything (except for a newline).
regex_pattern = r"...\....\....\....$"	# Do not delete 'r'.

import re

test_string1 = "123.456.abc.def"
test_string2 = "123.123.123.132.123.123"

match1 = re.match(regex_pattern, test_string1) is not None
match2 = re.match(regex_pattern, test_string2) is not None

print(str(match1).lower())
print(str(match2).lower())