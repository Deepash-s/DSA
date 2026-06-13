#left rotate - Brute

""" arr = [1, 2, 3, 4, 5, 6]
k = 2
n = len(arr)
k = k % n
temp = arr[:k]
for i in range(k, n):
    arr[i-k] = arr[i]
j = 0 
for i in range(n-k, n):
    arr[i] = temp[j]
    j += 1
print(arr) """

#right rotate - Brute

""" arr = [1, 2, 3, 4, 5, 6]
k = 2
n = len(arr)
k = k % n
temp = arr[n-k:]
for i in range(n-k-1, -1, -1):
    arr[k+i] = arr[i]
arr[:k] = temp
print(arr) """

#left rotate - optimal

""" arr = [1, 2, 3, 4, 5, 6]
k = 2
n = len(arr)
k = k % n
arr[:k] = reversed(arr[:k])
arr[k:] = reversed(arr[k:])
arr[:] = reversed(arr)
print(arr) """

#right rotate - optimal

arr = [1, 2, 3, 4, 5, 6]
k = 2
n = len(arr)
k = k % n
arr[:n-k] = reversed(arr[:n-k])
arr[n-k:] = reversed(arr[n-k:])
arr[:] = reversed(arr)
print(arr)