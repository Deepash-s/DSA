#largest number
def largestNum(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
            
    return largest

print(largestNum([1,32,43,74,22,44]))

#smallest number
def smallestNum(arr):
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
            
    return smallest

print(smallestNum([1,32,43,74,22,44]))