def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations={'+':add,
           '-':subtract,
           '*':multiply,
           '/':divide}
def calculator():
    num1= int(input('Whats is the first number?: '))
    calculating = True
    while calculating:
        for ops in operations:
            print(ops)
        operation= input('Choose an operation : ')
        num2= int(input('whats another number: '))
        result = operations[operation](num1,num2)
        print(f'{num1} {operation} {num2} = {result}')
        choice = input(f'Choose "y" to continue with previous  result {result} or else choose "n" to start again')
        if choice =='y':
            num1 = result
        else:
            calculating =False
            print('\n'*50)
            calculator()

calculator()

