#remove duplicates from sorted array

""" def removeDuplicates(arr):
    uni = set(arr)
    uni_arr = list(uni)
    return uni_arr

print(removeDuplicates([1,2,2,3,3,4,5,5])) """

""" def removeDuplicates(arr):
    if not arr:
        return []
    
    result = [arr[0]]
    
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            result.append(arr[i])
        
    return result

print(removeDuplicates([1, 2, 3, 3, 4, 5, 5])) """

#return number of unique with SC O(1)
def removeDuplicates(arr):
    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            arr[i+1] = arr[j]
            i += 1
            
    print(i+1)
    
removeDuplicates([1,1,2,2,2,3,3])