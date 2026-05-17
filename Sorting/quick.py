arr = [64, 25, 12, 22, 11]
n = len(arr)

def quicksort(arr, low, high):
    if low < high:
        partitionIndex = partition(arr, low, high)
        quicksort(arr, low, partitionIndex-1)
        quicksort(arr, partitionIndex+1, high)
        
def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    
    while i < j:
        while arr[i] <= pivot and i <= high-1:
            i += 1
        while arr[j] > pivot and j >= low+1:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        
        arr[low], arr[j] = arr[j], arr[low]
        return j
    
quicksort(arr, 0 ,4)

print(arr)