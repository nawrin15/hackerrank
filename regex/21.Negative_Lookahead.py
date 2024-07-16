# regex_1(?!regex_2)
# The negative lookahead (?!) asserts regex_1 not to be immediately followed by regex_2. 
# Lookahead is excluded from the match (do not consume matches of regex_2), 
# but only assert whether a match is possible or not.


# You have a test String S.
# Write a regex which can match all characters which are not immediately followed by that same character.

# Example

# If S = goooo, then regex should match ooo. Because the first g is not follwed by g 
# and the last o is not followed by o.

text1 = "goooo."
text2 = "gooloo"
text3 = "###$$$$"
text4 = "goluo" 
text5 = "gooooo"

Regex_Pattern = r"(.)(?!\1)"	# Do not delete 'r'.

import re


match = re.findall(Regex_Pattern, text1)
print(match)
print(text1, " Number of matches :", len(match))
match = re.findall(Regex_Pattern, text2)
print(match)
print(text2, " Number of matches :", len(match))
match = re.findall(Regex_Pattern, text3)
print(match)
print(text3, "Number of matches :", len(match))
match = re.findall(Regex_Pattern, text4)
print(match)
print(text4, "Number of matches :", len(match))
match = re.findall(Regex_Pattern, text5)
print(match)
print(text5, "Number of matches :", len(match))
