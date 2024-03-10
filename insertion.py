import time
start=time.time()
def insert(arr):
    for i in range(len(arr)):
        k=arr[i]
        j=i-1
        while j>=0 and k<arr[j]:
            arr[j+1]=arr[j]
            j-=1
            arr[j+1]=k
    return arr
arr=[23,13,1,65,43,32,56,12]
print(insert(arr))
end=time.time()
print(end-start)
