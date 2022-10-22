print('Simple calculator!')

print('Operations: + sum; - difference; * product; / quotient; ** exponent; % modulus')

first_number = int(input("First Number? "))
operation = input("Operation? ")
second_number = int(input("Second Number? "))

if operation == '+':
    final = first_number + second_number
    nome = 'sum'
elif operation == '-':
    final = first_number - second_number
    nome = 'difference'
elif operation == '*':
    final = first_number * second_number
    nome = 'product'
elif operation == '/':
    final = first_number / second_number
    nome = 'quotient'
elif operation == '**':
    final = first_number ** second_number
    nome = 'exponent'
elif operation == '%':
    final = first_number % second_number
    nome = 'modulus'
elif first_number.isnumeric() and second_number.isnumeric() == False:
    print('Please input a number.')
elif operation != '+' or '-' or '*' or '/' or '**' or '%':
    print('Operation not recognized.')

print (nome + ' of ' + str(first_number) + ' ' + operation + ' ' + str(second_number) + ' equals ' + str(final))


