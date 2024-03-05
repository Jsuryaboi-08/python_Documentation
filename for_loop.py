#for loops
import time
for i in range(5):
    print(i)

#range(start, stop, step)

for j in range(5, 10):
    print(j)

for k in range(0, 10, 2):
    print(k)

for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
print("Blastoff!")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
print(x)