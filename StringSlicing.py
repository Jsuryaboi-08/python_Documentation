#indexing[] and slicing[:] are used to extract a substring from a string

#indexing
#[start:stop:step]
#start is a numerical index for the slice start
#stop is the index you will go up to (but not include)
#step is the size of the jump you take

name = "jeya surya"
first_name = name[0:4]
first_name = first_name.capitalize()
print(first_name)
last_name = name[5:10]
print(last_name)
example = "0123456789"
example1= example[::2]#0,2,4,6,8
print(example1)
reversed_name = name[::-1]#-1 is the last character
#the above line is a common python trick to reverse a string

#slicing
#(start, stop, step)
website1 = "http://github.com"
slice = slice(7, -4)#start at 7, stop at -4
print(website1[slice])#github

