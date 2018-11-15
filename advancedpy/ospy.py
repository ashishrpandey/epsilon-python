import sys
import os

print(dir(sys))
os.chmod("myfile.txt",0777)
#os.mkdir("mynewdir")
#os.chdir("mynewdir")
#os.mkdir("anotherdir")
#os.chdir("anotherdir")
print (os.getcwd())
#print(os.environ)
print(os.getenv("HOME"))
print(os.__file__)
#print("\n")
#print(sys.executable)

#print(dir(sys))

#print(os.sys)


