"""
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', 'u'.
For example, if s = 'azcbobobegghakl', your program should print:
Number of vowels: 5
"""

import sys

vowels = ['a', 'e', 'i', 'o', 'u']

# default value for s
string = 'azcbobobegghakl'

# if s is given as an argument when file is run, change s
if len(sys.argv) > 1:
  string = sys.argv[1]

vowelCount = 0

# loop through each character in string
for character in string:
  if character in vowels:
    vowelCount += 1

print('Number of vowels:', vowelCount)