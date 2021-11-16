import math

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def square(x):
    return x*x

def sqrt(a):
    result = math.sqrt(a)
    return result

def exp(a):
    return a ** 2

def sin(x):
    result = math.sin(x)
    return result

def cos(x):
    result = math.cos(x)
    return result

def tan(x):
    result = math.tan(x)
    return result

print("""Choose a number for the following operations:
1. Addition(x,y)
2. Subtraction(a,b)
3. Multplication(a,b)
4. Divide(a,b)
5. Square(x)
6. Square root(x)
7. sin(x)
8. cos(x)
9. tan(x)""")
op = int(input('What operation do you want to perform:  '))

while op < 10:
    if op == 1:
        print('Enter parameters: ')
        x1 = int(input('enter x:    '))
        x2 = int(input('enter y:    '))
        print("Additon:     ",add(x1,x2))
    elif op == 2:
        print('Enter parameters: ')
        x1 = int(input('enter x:    '))
        x2 = int(input('enter y:    '))
        print("Subtraction:     ",subtract(x1,x2))
    elif op == 3:
        print('Enter parameters: ')
        x1 = int(input('enter x:    '))
        x2 = int(input('enter y:    '))
        print("Multiply:     ",multiply(x1,x2))
    elif op == 4:
        print('Enter parameters: ')
        x1 = int(input('enter x:    '))
        x2 = int(input('enter y:    '))
        print("Divide:     ",divide(x1,x2))
    elif op == 5:
        print('Enter parameters: ')
        x = int(input('enter x:    '))
        print("Square:     ",square(x))
    elif op == 6:
        print('Enter parameters: ')
        x = int(input('enter x:    '))
        print("Square root:     ",sqrt(x))
    elif op == 7:
        print('Enter parameters: ')
        x = int(input('enter x:    '))
        print("sin(x):     ",sin(x))
    elif op == 8:
        print('Enter parameters: ')
        x = int(input('enter x:    '))
        print("cox(x):     ",cos(x))
    elif op == 9:
        print('Enter parameters: ')
        x = int(input('enter x:    '))
        print("tan(x):     ",tan(x))
    else:
        print('choose another operation')

    new = int(input('Do you want to continue yes(1)/no(0):  '))
    if new == 1:
        op = int(input('enter operation:    '))
    elif new == 0:
        print('Goodbye! :)')
        break

    