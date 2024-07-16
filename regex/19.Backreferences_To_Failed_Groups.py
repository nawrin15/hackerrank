# Backreference to a capturing group that match nothing is different from backreference 
# to a capturing group that did not participate in the match at all.

# Capturing group that match nothing

# Here, b? is optional and matches nothing.
# Thus, (b?) is successfully matched and capture nothing.
# o is matched with o and \1 successfully matches the nothing captured by the group.

# Capturing group that didn't participate in the match at all


# In most regex flavors (excluding JavaScript), (b)?o\1 fails to match o.
# Here, (b) fails to match at all. Since, the whole group is optional the regex engine 
# does proceed to match o.
# The regex engine now arrives at \1 which references a group that did not participate 
# in the match attempt at all.
# Thus, the backreference fails to match at all.

# You have a test string S.
# Your task is to write a regex which will match S, with following condition(s):

#  S consists of 8 digits.
#  S may have "" separator such that string S gets divided in 4 parts, with
#  each part having exactly two digits. (Eg. 12-34-56-78)

Regex_Pattern = r"^\d\d(-?)\d\d\1\d\d\1\d\d$"	# Do not delete 'r'.

import re

text1 = "12-34-56-78"
text2 = "12345678"
text3 = "12-34-56-78-88"
text4 = "1-234-56-78"

print(str(bool(re.search(Regex_Pattern, text1))).lower())
print(str(bool(re.search(Regex_Pattern, text2))).lower())
print(str(bool(re.search(Regex_Pattern, text3))).lower())
print(str(bool(re.search(Regex_Pattern, text4))).lower())