n = int(input('Enter array Size: '))
arr = []
mp = {}

for i in range(n):
    num = int(input(f"Enter element {i}: "))
    arr.append(num)
    mp[num] = mp.get(num, 0) + 1
    
queries = int(input("Enter number of queries: "))

for i in range(queries):
    q = int(input("Enter element to find frequency: "))
    print(mp.get(q, 0))