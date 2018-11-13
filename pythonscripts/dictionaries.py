# key value pairs
# ordered
# fast access 

address = {"fname":"ashish", "lname":"Pandey"}
print(address["fname"])


#address2 = {"name": { "fname":"ashish", "lname":"Pandey"}}

#print(address2["name"]["fname"])
address["pincode"] = "227807"
address["fname"] = "ASHISH"
print(address)
'''
if "fname" not in address.keys():
	address["fname"] = "Ashish"
'''

print(list(address.keys()))
print(list(address.values()))
print(list(address.items()))

for k,v in address.items():
	print(k + v)

#print(dir(dict))

i = address.pop("fname")


print(i)
print(address)
'''
v = address["fname"]
#print(help(address.pop))
print(i)
print(address)
#print(dir(address))

'''
