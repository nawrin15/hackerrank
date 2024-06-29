#The negated character class [^] matches any character that is not in the square brackets.
# Task

# You have a test string S.
# Your task is to write a regex that will match  with the following conditions:

# S must be of length 6.
# First character should not be a digit ( 1,2,3,4,5,6,7,8,9 or 0 ).
# Second character should not be a lowercase vowel ( a,e,i,o or u ).
# Third character should not be b, c, D or F.
# Fourth character should not be a whitespace character ( \r, \n, \t, \f or <space> ).
# Fifth character should not be a uppercase vowel ( A,E,I,O or U ).
# Sixth character should not be a . or , symbol.

Regex_Pattern = r'^[^1234567890][^aeiou][^bcDF][^\r\n\t\f\s][^AEIOU][^.,]$'	
Regex_Pattern1 = r'^[^0-9][^aeiou][^bcDF][^\s][^AEIOU][^.,]$'	
Regex_Pattern2 = r'^\D[^aeiou][^bcDF]\S[^AEIOU][^.,]$'	

import re
text1 = "think?"
text2 = "think??"
text3 = "athink?"
print(str(bool(re.search(Regex_Pattern, text1))).lower())
print(str(bool(re.search(Regex_Pattern, text2))).lower())
print(str(bool(re.search(Regex_Pattern, text3))).lower())

print(str(bool(re.search(Regex_Pattern1, text1))).lower())
print(str(bool(re.search(Regex_Pattern1, text2))).lower())
print(str(bool(re.search(Regex_Pattern1, text3))).lower())

print(str(bool(re.search(Regex_Pattern2, text1))).lower())
print(str(bool(re.search(Regex_Pattern2, text2))).lower())
print(str(bool(re.search(Regex_Pattern2, text3))).lower())