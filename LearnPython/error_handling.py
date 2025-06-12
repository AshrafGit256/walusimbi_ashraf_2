# Python error handling

# Define Error
# Errors occur when a program encounters unexpected situations during execution

# Types of errors

# 1: Syntax errors
# 2: Runtime erros  5/0
# 3: Logical errors

# Block of codes try, except, else and finally

# 1: try
# 2: except
# 3: else
# 4: finally

# Example four try to divide 5 / 0 (cause ZeroDivisionError)

# try:
#     result = 5 / 2

# except ZeroDivisionError:
#     print('Cannot divde by zero. ')

# else:
#     print('Divion successful', result)

# finally:
#     print('run completed')


# Execrise Five:
# Raise a custom exception that checks for positive number .

# class NotPositiveNumber(Exception):
#     pass

# def checkNumber(n):
#     if n<=0:
#         raise NotPositiveNumber('Number is negative')
    
# try:
#     n = int(input('Enter a number: '))
#     checkNumber(n)
# except NotPositiveNumber as e:
#     print("Error:",e)
# else:
#     print("The number is +ve :",n)
# finally:
#     print('Done with check')


# Assignment Two:
# Write a program to handle errors, the program should ask for two number using input and then
# divides them. Use an infinite loop to keep asking until a valid input is provide.

class NotPositiveNumber(Exception):
    pass

def checkNumber(n):
    if n<=0:
        raise NotPositiveNumber('Number is negative')
    
while True:
    try:
        num1 = int(input('Enter 1st number: '))
        num2 = int(input('Enter 2nd number: '))
        n = num1 / num2
        checkNumber(n)
    except NotPositiveNumber as e:
        print("Error:",e)
    except ValueError:
        print('Error:',e)
    else:
        print("The number is +ve :",n)
        break
    finally:
        print('Done with check')
        print()
