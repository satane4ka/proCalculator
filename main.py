#Calcualtor 
#Python version 3.12.3 and later

'''
Improved version of calculator with functions, but without checking all kinds of mistakes, especially with numbers

Solved the problem when the user entered an incorrect operation, after which the program closed
'''


def sum(num1 : float, num2 : float) -> float:
    answer = num1 + num2
    return answer


def diff(num1 : float, num2 : float) -> float:
    answer = num1 - num2
    return answer


def mult(num1 : float, num2 : float) -> float:
    answer = num1 * num2
    return answer


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


#TODO make block try/except to avoid problem with incorrect numbers input 
def main():
    print('Calculator')

    OPERATION_LIST = ['+', '-', '*', '/']
    
    result = float(input('Enter first number: ')) # For first iteration it will be first number, after that it will be like a previous result
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


if __name__ == '__main__':
    main()