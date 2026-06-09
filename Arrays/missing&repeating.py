#brute

""" arr = [3, 5, 4, 1, 1]
n = len(arr)
repeating = missing = -1

for i in range(1, n):
    count = 0
    for j in range (n):
        if arr[j] == i:
            count += 1
    if count == 2:
        repeating = i
    elif count == 0:
        missing = i
    if missing != -1 and count != -1:
        break
        
print(f"Missing: {missing}\nRepeating: {repeating}") """

#better - hashing

""" arr = [3, 5, 4, 1, 1]
n = len(arr)
repeating = missing = -1

freq = [0] * (n+1)
for i in range(n):
    freq[arr[i]] += 1
    
for i in range(1, n):
    if freq[i] == 2:
        repeating = i
    elif freq[i] == 0:
        missing = i
    if repeating != -1 and missing != -1:
        break

print(f"Missing: {missing}\nRepeating: {repeating}") """

arr = [3, 5, 4, 1, 1]
n = len(arr)
s = s2 = 0
sn = (n * (n+1)) // 2
s2n = (n * (n+1) * (2*n+1)) // 6 

for num in arr:
    s += num
    s2 += num * num

val1 = s - sn
val2 = s2 - s2n
val2 = val2 // val1
x = (val1 + val2) // 2
y = val2 - x
print(f"Missing: {y}\nRepeating: {x}")
