import time
start=time.time()

def bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i -1):
            if arr[j+1]<arr[j]:
                arr[j+1],arr[j]=arr[j],arr[j+1]
    return arr
arr=[23,13,1,65,43,32,56,12]
print(bubble(arr))
end=time.time()
print(end-start)

