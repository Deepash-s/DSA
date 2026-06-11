""" arr = [1, 2, 3, 4, 5] 
last = arr.pop(len(arr)-1)
arr.insert(0, last)
print(arr) """

#right rotate (clockwise)
""" arr = [1, 2, 3, 4, 5] 
n = len(arr)
temp = arr[0]
for i in range(1, n):
    arr[i-1] = arr[i]
    
arr[n-1] = temp
print(arr) """

#left rotate (anti-clockwise)
arr = [1, 2, 3, 4, 5] 
n = len(arr)
temp = arr[n-1]
for i in range(n-1, 0, -1):
    arr[i] = arr[i-1]
    
arr[0] = temp
print(arr)