# Parenthesis ( ) around a regular expression can group that part of regex together. This allows us to apply different quantifiers to that group.

# These parenthesis also create a numbered capturing. It stores the part of string matched by the part of regex inside parentheses.

# These numbered capturing can be used for backreferences.

# (?: ) can be used to create a non-capturing group. It is useful if we do not need the group to capture its match.

# Task

# You have a test String S.
# Your task is to write a regex which will match S with the following condition:

# S should have 3 or more consecutive repetitions of ok.

text = "okokok! cya"

Regex_Pattern = r'(ok){3,}'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, text))).lower())