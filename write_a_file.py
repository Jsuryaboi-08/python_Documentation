text = "hello from python"

with open('test.txt', 'a') as file:#w - write, r - read, a - append
    file.write(text)