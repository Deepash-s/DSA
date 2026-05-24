""" def secondLargestNum(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    
    sLargest = -1
    
    for num in arr:
        if num > sLargest and num != largest:
            sLargest = num
            
    return sLargest

print(secondLargestNum([1,32,43,74,22,44])) """

#optimal approach

def secondLargest(arr):
    """ largest = arr[0]
    sLargest = -1 """
    largest = sLargest = float('-inf')
    
    for num in arr:
        if num > largest:
            sLargest = largest
            largest = num
        elif num < largest and num > sLargest:
            sLargest = num
            
    return sLargest if sLargest != float('-inf') else None

print(secondLargest([-1,-32,-43,-74,-22,-44]))