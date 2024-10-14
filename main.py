#Calcualtor 
#Python version 3.12.3

'''
Simple version of Calculator on Python without functions, try catch, checking types of variables and OOP

The process will be stopped, if you don't input operation from OPERATION_LIST
'''


OPERATION_LIST = ['+', '-', '*', '/']

num1 = int(input('Input first number: '))
num2 = int(input('Input second number: '))
operation = input('Input operation: ')
result = 0

while operation in OPERATION_LIST:
    if operation == '+':
        result = num1 + num2
        print(f'Result: {result}')
    elif operation == '-':
        result = num1 - num2
        print(f'Result: {result}')
    elif operation == '*':
        result = num1 * num2
        print(f'Result: {result}')
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f'Result: {result}')
        else:
            while num2 == 0:
                num2 = int(input('Input second number again: '))
            result = num1 / num2
            print(f'Result: {result}')
    
    num1 = result
    num2 = int(input('Input second number: '))
    operation = input('Input operation: ')
    