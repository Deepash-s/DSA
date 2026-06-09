arr = [0,0,1,1,1,2,2,3,3,4]

def removeDuplicates(arr):
    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            arr[i+1] = arr[j]
            i += 1
    
    return i+1

print(removeDuplicates(arr))
print(arr)