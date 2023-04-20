#!/usr/bin/python
import re

line = 'your alpha@scientificprograming.io, blah beta@scientificprogramming.io blah user'

emails = re.findall(r'[\w\.-]+@[\w\.-]+', line)    

if emails:
  print(emails)
else:
  print("No match!")