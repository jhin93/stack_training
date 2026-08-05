# Modify the scaffold code to use the findall function and output every occurrence of the string python in a line provided by the user.  Your search must be case insensitive.  If the string is not found, you must return the string No pythons here! Do not change the input prompt message.

# For example, given the user input

# The Python is case sensitive so PYTHON is not the same as python 
# You output would be:

# ['Python', 'PYTHON', 'python']

#!/bin/env python3
import re

#We prompt the user
read_text = input("Enter some text\n")

#Write some regex in the variable test_regx to produce our desired match.
test_regx = r"python"

#add options to findall if necessary if not fix the code.
find_list = re.findall(test_regx,read_text,re.IGNORECASE)

if len(find_list) != 0:
    print(find_list)
else:
    print('No pythons here!')