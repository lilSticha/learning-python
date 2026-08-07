
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b ==0 or a == 0:
        return 'Error: Division by zero'
    else: return a/b


a = float(input('First number:'))
sign = input('Enter the operation (+, -, *, /):')
b = float(input('Second number:'))

if sign == '+':
    print(add(a,b))
elif sign == '-':
    print(subtract(a,b))
elif sign == '*':
    print(multiply(a,b))
elif sign == '/':
    print(divide(a, b))
else : 
    print('Invalid operation')

          # test comment
