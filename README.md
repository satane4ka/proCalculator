# Calculator

## A functional style calculator where each function performs only one task

**The entire program is divided into separate blocks, where each block is a function that solves its own specific problem. This program has functions corresponding to the simplest mathematical operations, For example:**

```python
def sum(...)

def diff(...)

def mult(...)

def div(...)

def calculation(...)

def main(...)
```


## Sum function

```python
def sum(num1 : float, num2 : float) -> float:
    answer = num1 + num2
    return answer
```
**The signature of this function shows that it takes two numbers of type `float` as parameters and returns a number of type `float`**


## Difference function

```python
def diff(num1 : float, num2 : float) -> float:
    answer = num1 - num2
    return answer
```
**The signature of this function shows that it takes two numbers of type `float` as parameters and returns a number of type `float`**


## Multiplication function

```python
def mult(num1 : float, num2 : float) -> float:
    answer = num1 * num2
    return answer
```
**The signature of this function shows that it takes two numbers of type `float` as parameters and returns a number of type `float`**


## Division function
```python
def div(num1 : float, num2 : float) -> float:
    if num2 == 0:
        while num2 == 0:
            print('WARNING! You cannot divide by "0"!')
            num2 = float(input('Please input new second number: '))
        answer = num1 / num2
        return answer
    else:
        answer = num1 / num2
        return answer
```
**The signature of this function shows that it takes two numbers of type `float` as parameters and does not return a number of type `float`, but in this function there is a check for the error of division by `0`, if the user selects the division sign and writes `0` as the second number, then the program asks him to enter another number, since division by `0` is impossible**


## Calculation function

```python
def calculation(num1 : float, num2 : float, op : str) -> float:
    match op:
        case '+':
            return sum(num1, num2)
        case '-':
            return diff(num1, num2)
        case '*':
            return mult(num1, num2)
        case '/':
            return div(num1, num2)
```
**The signature of this function shows that it takes two numbers of type `float` and operation sign of type `str` as parameters and returns a number of type `float`**


## Main function

```python
def main():
    print('Calculator')

    OPERATION_LIST = ['+', '-', '*', '/']
    
    number1 = float(input('Enter first number: '))
    result = number1 #For first iteration in loop
    while True:
        operation = input('Enter operation: ')
        if operation not in OPERATION_LIST:
            while operation not in OPERATION_LIST:
                print('\nTo stop working inputp "stop"')
                print('Else enter operation from list(+, -, *, /)')
                operation = input('\nEnter new operation value: ')
                if operation.lower() == 'stop':
                    break

        if operation.lower() == 'stop':
            print('Thank you for using of this calculator!')
            break
            
        number2 = float(input('Enter second number: '))
        result = calculation(result, number2, operation)
        print(f'Result: {result}', sep='\n')
```




## Solving the problem of previous version of program
**This version of the calculator solves the problem of its predecessor, due to which the program ended instantly if an incorrect `operation` sign was entered. We managed to achieve this using this block of code:**

```python
OPERATION_LIST = ['+', '-', '*', '/']

    number1 = float(input('Enter first number: '))
    result = number1 #For first iteration in loop
    while True:
        operation = input('Enter operation: ')
        if operation not in OPERATION_LIST:
            while operation not in OPERATION_LIST:
                print('\nTo stop working inputp "stop"')
                print('Else enter operation from list(+, -, *, /)')
                operation = input('\nEnter new operation value: ')
                if operation.lower() == 'stop':
                    break

        if operation.lower() == 'stop':
            print('Thank you for using of this calculator!')
            break
```

