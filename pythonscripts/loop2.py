# Conditionals 
s = "5th training in Epsilon"
vowel = "aeiou"

#for i in s:
#	print(i)
i = 0
while(i < len(s)):
	if(s[i] in vowel):
		#print('got a vowel "' , s[i] ,'" breaking now')
		i += 1 
		pass
	print(s[i])
	i += 1 







'''
if (s[0] in vowel):
	print(s[0])
	print("1st charecter is a vowel")
	print("still in if block")
elif(s[0].isdigit()):
	print("1st char is a digit")
else:
	print("1st char is neither a vowel nor a digit")
print("out of if-else block")
'''
