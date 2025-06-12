#lambda functions

# Definition
# It is used for small functions, and we use a lambda key word


# def add(a, b): return a + b

# print(add(10, 5))

# square = lambda  x: x*x
# print(square(2))

# add = lambda a, b : a + b
# print(add(10, 5))

# numbers = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x*x, numbers))
# print(squared)


# Assignment one : Find the factorial of a number (five)

def factorial_of_5(a,b,c,d,e):
    factorial = lambda a,b,c,d,e: a*b*c*d*e
    print(factorial(a,b,c,d,e))
factorial_of_5(1,2,3,4,5)