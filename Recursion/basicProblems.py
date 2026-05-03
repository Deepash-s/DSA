""" def prints(count):
    if(count>5):
        return
    print(count)
    count += 1
    prints(count)
    
prints(1) """

""" def prints(count):
    if(count<1):
        return
    print(count)
    count -= 1
    prints(count)
    
prints(10) """


""" def prints(i, n):
    if(i<1):
        return
    prints(i-1, n)
    print(i)
    
prints(10, 10) """

""" def prints(i, n):
    if(i>n):
        return
    prints(i+1, n)
    print(i)
    
prints(1, 10) """