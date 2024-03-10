import time
start=time.time()
def qs(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot=arr[0]
        less=[x for x in arr[1:] if x <= pivot]
        greater = [y for y in arr[1:] if y > pivot ]
        return qs(less)+[pivot]+qs(greater)

arr=[21,432,1,3,21,9,22]
print(qs(arr))
end=time.time()
print(end-start)
        
