arr = [1, 2, 3, 4, 5, 6, 8]
n = len(arr)+1
expected_sum = n*(n+1)//2
actual_sum = sum(arr)
missing_number = expected_sum - actual_sum
print(missing_number)

""" for i in range(1, n-1):
    if(arr[i]-1 != arr[i-1]):
        print(arr[i]-1)
        break """