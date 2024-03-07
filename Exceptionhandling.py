try:
    a = 10/0
    print(a)
except Exception:
    print("An error occurred")

try:
    nume = int(input("enter a number: "))
    denom = int(input("enter a number: "))
    result = nume/denom
except ZeroDivisionError as e:#if the denominator is zero
    print("division by zero")
except ValueError as e:#if the input is not a number
    print("invalid input")
else:
    print(result)
finally:
    print("executed")#executed no matter what
    