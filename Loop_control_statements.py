#break 
#continue
#pass


while True:
    name = input("Enter your name: ")
    if name != "":
        break

phone_number = "123-456-7890"
for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

#pass acts as a placeholder
for i in range(1,21):
    if i == 21:
        pass
    else:
        print(i)