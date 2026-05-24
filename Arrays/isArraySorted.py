def isArraySorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
        
    return True

print(isArraySorted([1,2,1,7,8,11]))