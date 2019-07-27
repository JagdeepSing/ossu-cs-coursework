"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
"""

import sys

# default value for s
string = 'azcbobobegghakl'

# if s is given as an argument when file is run, change s
if len(sys.argv) > 1:
  string = sys.argv[1]

start = 0
longest = ''

for i in range(0, len(string) - 1):
  if string[i] <= string[i + 1]:
    if len(string[start:i + 2]) > len(longest):
      longest = string[start:i + 2]
    end = i + 1
  else:
    start = i + 1

print('Logest substring in aplhabetical order is:', longest)