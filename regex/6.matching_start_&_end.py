#The ^ symbol matches the position at the start of a string.
#The $ symbol matches the position at the end of a string.

# You have a test string S. Your task is to match the pattern Xxxxx
# Here, x denotes a word character, and X denotes a digit.
# must start with a digit X and end with . symbol.
# S should be 6 characters long only.

Regex_Pattern = r"^\d\w\w\w\w.$"	# Do not delete 'r'.

import re
text = "0qwer."
print(str(bool(re.search(Regex_Pattern, text))).lower())