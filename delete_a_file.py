import os
import shutil
path = "delete.txt"
try:
    os.remove(path)
    #os.rmdir("empty_folder") only delete empty folder
    #shutil.rmtree("empty_folder")#delete folder with files
except FileNotFoundError:
    print(f"File not found: {path}")
except PermissionError:
    print(f"You don't have permission to delete: {path}")
except OSError as e:
    print(f"Error: {e.strerror}")
else:
    print(f"File deleted: {path}")



