#\s matches any whitespace character [ \r\n\t\f ].
#\S matches any non-white space character.
#You have a test string . Your task is to match the pattern 
#Here,  denotes whitespace characters, and  denotes non-white space characters.

Regex_Pattern = r"\S\S\s\S\S\s\S\S"	# Do not delete 'r'.

import re
text = "12 11 15"
print(str(bool(re.search(Regex_Pattern, text))).lower())