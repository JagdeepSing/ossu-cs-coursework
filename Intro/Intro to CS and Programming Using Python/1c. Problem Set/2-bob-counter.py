"""
Assume s is a string of lower case characters.

Write a program that prints the number of times 
the string 'bob' occurs in s. For example, if 
s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2
"""

import sys

# default value for s
string = 'azcbobobegghakl'

# if s is given as an argument when file is run, change s
if len(sys.argv) > 1:
  string = sys.argv[1]

bobCount = 0

for i in range(0, len(string) - 2):
  if string[i] == 'b':
    if string[i+1] == 'o': 
      if string[i+2] == 'b':
        bobCount += 1
      else:
        i += 3
    else:
      i += 1
  else:
    i += 1

print('Number of times bob occurs is:', bobCount)