a = [3, 5, 2, 5, 2]
b = [2, 3, 5, 5, 2]

freq = {}

for num in a:
    freq[num] = freq.get(num, 0) + 1
  
equal = True  
for num in b:
    if num not in freq:
        equal = False
        break
    elif freq[num] == 0:
        equal = False
        break
    freq[num] -= 1
    
if equal:
    print("Arrays are equal")
else:
    print("Arrays are not equal")