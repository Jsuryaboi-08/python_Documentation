import os

source = "move.txt"
destination = "C:\\Users\\winje\\OneDrive\\Desktop\\1\\move.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there.")
    else:
        os.replace(source, destination)
        print(source + " was moved to " + destination)
except FileNotFoundError:
    print(source + " does not exist");
    
