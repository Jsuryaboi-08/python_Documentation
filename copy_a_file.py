import shutil
#copyfile() will copy the contents of the source file to the destination file.
#copy() will copy the file at the path source to the file or directory at the path destination and will return the full path to the new file.
#copy2() will copy the file at the path source to the file or directory at the path destination and will preserve the original file's metadata.

shutil.copyfile('test.txt','copy.txt')#src, dst, *, follow_symlinks=True)
#can cpoy to a different directory. we should specify the path insted of just copy.txt

shutil.copy('test.txt','copy.txt')#src, dst, *, follow_symlinks=True)
#copy will copy the file at the path source to the file or directory at the path destination and will return the full path to the new file.   
shutil.copy2('test.txt','copy.txt')#src, dst, *, follow_symlinks=True)
#copy2 will preserve the original file's metadata.
