def maxOccurring(arr):
    mp = {}
    for num in arr:
        mp[num] = mp.get(num, 0) + 1
        
    print(max(mp ,key=mp.get))
    
maxOccurring([1,3,2,3,5,5,3])