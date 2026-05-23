arr = []
n = int(input("Enter Array size: "))

for i in range(n):
    arr.append(int(input(f"Enter Element {i}: ")))
    
hash_arr = [0] * (n + 1)

for num in arr:
    hash_arr[num] += 1
    
q = int(input("Enter number of queries: "))

while(q):
    number = int(input("Enter number to find frequency:"))
    q -= 1
    print(f"Frequency of {number}: {hash_arr[number]}")