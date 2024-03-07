import os
with open('test.txt') as file:#opens the file and closes it after the block
    print(file.read())
    #doesnt handle the exception if the file does not exist

try:
    with open('test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("The file does not exist")
#handles the exception if the file does not exist