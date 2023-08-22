import math
def main():
    print("Enter:\n1 - addition\n2 - subtraction\n3 - multiplication\n4 - division"
          "\n5 - modulus\n6 - square root\n7 - exponent\n8 - exit")

def repeat(n):
    if n == 1:
        a,b = input("enter 2 numbers to add: \n").split()
        add(a,b)
        rapo()
    elif n == 2:
        a,b = input("enter 2 numbers to subract: \n").split()
        sub(a,b)
        rapo()
    elif n == 3:
        a, b = input("enter 2 numbers to multiply: \n").split()
        mul(a, b)
        rapo()
    elif n == 4:
        a, b = input("enter 2 numbers to divide: \n").split()
        div(a, b)
        rapo()
    elif n == 5:
        a, b = input("enter 2 numbers to perform modulus operation: \n").split()
        mod(a, b)
        rapo()
    elif n == 6:
        a = float(input("enter a number to perform square root: \n"))
        print(math.sqrt(a))
        rapo()
    elif n == 7:
        a, b = input("enter 2 numbers to perform exponentiation: \n").split()
        expo(a, b)
        rapo()
    elif n == 8:
        return 0

def add(x,y):
    print(float(x)+float(y))

def sub(x,y):
    print(float(x) - float(y))

def mul(x,y):
    print(float(x) * float(y))

def div(x,y):
    print(float(x) // float(y))

def mod(x,y):
    print(float(x) % float(y))

def expo(x,y):
    print(float(x) ** float(y))

def rapo():
    s = int(input("Enter the number to continue the process: "))
    repeat(s)

print("Calculator")
main()
val = int(input("Enter the number: "))
repeat(val)
