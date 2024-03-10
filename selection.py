import time
start=time.time()
def selection(arr):
    for i in range(len(arr)):
        m = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[m]:
                m = j
        arr[i], arr[m] = arr[m], arr[i]
    return arr

arr = [23, 13, 1, 65, 43, 32, 56, 12]
print(selection(arr))
end=time.time()
print(end-start)
