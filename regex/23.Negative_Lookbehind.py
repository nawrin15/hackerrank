# (?<regex_2)regex_1
#The negative lookbehind (?<!) asserts regex_1 not to be immediately preceded by regex_2. 
# Lookbehind is excluded from the match (do not consume matches of regex_2), 
# but only assert whether a match is possible or not.

# Task

# You have a test String S.
# Write a regex which can match all the occurences of characters 
# which are not immediately preceded by vowels (a, e, i, u, o, A, E, I, O, U).


Regex_Pattern = r"(?<![a-z])[aeiou]"

import re

Test_String = "he1o"

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match), match)

Regex_Pattern = r"(?<![aeiouAEIOU])(.)"

Test_String = "1o1s"

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match), match)

Test_String = "thisisavowel"

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match), match)

Test_String = "1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik9ool./;p01QAZ2WSX3EDC4RFV5TGB6YHN7UJM8IK,9OL.0P;/-['"

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match), match)

Test_String = "SC HUIEHKESYG VSBC SF BDS GUIHuhjsd bcukhb2ip4hjjvs bvfdsbvl bv"

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match), match)