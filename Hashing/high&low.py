def highAndLow(arr):
    mp = {}
    for num in arr:
        mp[num] = mp.get(num, 0) + 1
    high_freq = max(mp.values())
    low_freq = min(mp.values())

    high = [k for k, v in mp.items() if v == high_freq]
    low = [k for k, v in mp.items() if v == low_freq]
    
    print(f'''highest frequent: {min(high)}\nlowest frequent: {min(low)}''')

highAndLow([1,2,2,1,1,4])