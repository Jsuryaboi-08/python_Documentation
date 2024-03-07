#index operator [] is used to access elements of a sequence(str, list, tuple)

name = "surya"
if name[0] == 's':
    print('s is present')

if name[1].islower():
    name = name.capitalize()

New_name="jeya surya"

first_name = New_name[:4].upper()
print(first_name)

last_name = New_name[5:].capitalize()
print(last_name)

last_charecter = New_name[-1]
print(last_charecter)

