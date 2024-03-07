import os

path = "C:\\Users\\winje\\OneDrive\\Desktop\\test.txt"

if os.path.exists(path):#checks if the file exists
    print("The file exists")
    if os.path.isfile(path):
        print("that is a file")
    elif os.path.isdir(path):#checks if the path is a directory
        print("that is a directory")
else:
    print("The file does not exist")
