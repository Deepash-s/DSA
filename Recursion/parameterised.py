""" def total_sum(i, sum):
    if i<1:
        print(sum)
        return
    total_sum(i-1, sum+i)
    
total_sum(5, 0) """

def factorial(i, fact):
    if i<1:
        print(fact)
        return
    factorial(i-1, fact*i)
    
factorial(5, 1)