#The expression \D matches any character that is not a digit.
#The expression \d matches any digit [ - ].

#You have a test string . Your task is to match the pattern 
#Here  denotes a digit character, and  denotes a non-digit character.

import re
Regex_Pattern = r"\d\d\D\d\d\D\d\d\d\d"	# Do not delete 'r'.
text = "06-11-2015"
print(str(bool(re.search(Regex_Pattern, text))).lower())