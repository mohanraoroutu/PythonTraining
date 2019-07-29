#os.path.exists()

import os.path
from os import path

def main():

   print("file exist:"+str(path.exists('CheckFileStatus.py')))
   print("File exists:" + str(path.exists('mohanCheckFileStatus.py')))
   print("directory exists:" + str(path.exists('myDirectory')))

if __name__== "__main__":
   main()

# #os.path.isfile()

# import os.path
# from os import path

def main():

    print("Is it File?" + str(path.isfile('guru99.txt')))
    print("Is it File?" + str(path.isfile('myDirectory')))

if __name__== "__main__":
main()


#os.path.isdir()

import os.path
from os import path

def main():

print("Is it Directory?" + str(path.isdir('guru99.txt')))
print("Is it Directory?" + str(path.isdir('myDirectory')))
#print("Is it Directory?" + str(path.isdir('myWorldMohan')))


if __name__== "__main__":
main()


#pathlibPath.exists()

import pathlib
file = pathlib.Path("guru99.txt")
if file.exists ():
print("File exist")
else:

print("File not exist")

import os
from os import path

def main():
# Print the name of the OS
    print(os.name)
#Check for item existence and type
print("Item exists:" + str(path.exists("guru99.txt")))
print("Item is a file: " + str(path.isfile("guru99.txt")))
print("Item is a directory: " + str(path.isdir("guru99.txt")))

if __name__ == "__main__":
main()
