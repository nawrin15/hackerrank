#The expression \w will match any word character.
#Word characters include alphanumeric characters (-, - and -) and underscores (_).

#\W matches any non-word character.
#Non-word characters include characters other than alphanumeric characters (-, - and -) and underscore (_).

Regex_Pattern = r"\w\w\w\W\w\w\w\w\w\w\w\w\w\w\W\w\w\w"	# Do not delete 'r'.

import re
text = "www.hackerrank.com"
print(str(bool(re.search(Regex_Pattern, text))).lower())