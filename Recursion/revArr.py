arr = [64, 25, 12, 22, 11]
n = len(arr)

def reverse(l, r):
    if l >= r:
        return
    arr[l], arr[r] = arr[r], arr[l]
    reverse(l+1, r-1)
    
reverse(0, 4)
print(arr)

arr2 = [64, 25, 12, 22, 11]
n2 = len(arr)

def reverse2(i):
    if i >= n2/2:
        return
    arr2[i], arr2[n-i-1] = arr2[n-i-1], arr2[i]
    reverse2(i+1)
    
reverse2(0)
print(arr2)