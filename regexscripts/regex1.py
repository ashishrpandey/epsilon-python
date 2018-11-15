# pattern validation 
# pattern extraction 

import re 

s = "abcdabddacacadede"
#r = re.compile("ab[c,d]")
#l = re.findall(r,s)
#print(l)

# metachars :
# . = > mathch with anything 
# [a-z] [A-Z][a-zA-Z]=> char class
# digit [0-9] => digit class
# + => atleast one occurance if more allowed
# * => zero more occurance 
# ^ =>start of the string 
# $ => end of the string
# [a-z]{4} => 4 chars
# [0-9]{2,4} => 2 to 4 
# s = "abcd124"
# r = re.compile("^[a-z]{2,4}[0-9]+$")
# l = re.findall(r,s)
# print(l)

s = "AAABCDE134AFGFH242D"
r = re.compile("[A-Z]{2}[0-9]{3}[A-Z]")

#fileobj = open("filename.log","r")
#l = re.findall(r,fileobj.read())
l = re.findall(r,s)

print(l)
