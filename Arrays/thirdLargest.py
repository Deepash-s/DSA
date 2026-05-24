def thirdLargest(arr):
    first = second = third = float('-inf')
    
    for num in arr:
        
        if num > first:
            third = second
            second = first
            first = num
        
        elif first > num > second:
            third = second
            second = num
            
        elif second > num > third:
            third = num
            
    return third if third != float('-inf') else None

print(thirdLargest([-1,-32,-43,-74,-22,-44]))
print(thirdLargest([1,32,43,74,44,22,44]))
