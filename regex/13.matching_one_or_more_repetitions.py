# The + tool will match one or more repetitions of character/character class/group.

# For Example:


# w+ : It will match the character w 1 or more times.
# [xyz]+ : It will match the character x, y or z 1 or more times.
# \d+ : It will match any digit 1 or more times.

# Task

# You have a test string S.
# Your task is to write a regex that will match S using the following conditions:

# S should begin with 1 or more digits.
# After that, S should have 1 or more uppercase letters.
# S should end with 1 or more lowercase letters


Regex_Pattern = r'^\d{1,}[A-Z]+[a-z]+$'	# Do not delete 'r'.

import re
text1 = "1Qa"
print(str(bool(re.search(Regex_Pattern, text1))).lower())
