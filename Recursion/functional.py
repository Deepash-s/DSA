""" def total(n):
    if n == 0:
        return 0
    return n + total(n-1)

print(total(5)) """

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))