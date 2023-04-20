#!/usr/bin/python
import re

line = 'your alpha@scientificprograming.io, blah beta@scientificprogramming.io blah user'
# emails = re.findall(r'[\w\.-]+@[\w\.-]+', line)    
# emails = re.findall(r'\w+\s(\w+@\w+\.\w+)\s\w+\s(\w+@\w+\.\w+)\s(\w+)\s(\w+)', line)    
emails = re.findall(r'\S(\w+@\w+\.\w+)', line)    

if emails:
  for email in emails:
    print(email[0])
  print(emails)
else:
  print("No match!")