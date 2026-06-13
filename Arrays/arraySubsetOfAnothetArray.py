a = [11, 7, 1, 13, 21, 3, 7, 3]
b = [11, 3, 7, 1, 7]

""" hash_set = set(a)
res = True
for num in b:
    if num not in hash_set:
        res = False
        break
    
print(res) """

def isSubset(a, b):
    freq = {}
    for num in a:
        freq[num] = freq.get(num, 0) + 1
        
    for num in b:
        if num not in freq or freq[num] == 0:
            return False
        freq[num] -= 1
            
    return True

print(isSubset(a, b))