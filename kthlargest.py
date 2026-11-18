arr=[10,45,67,89,28]
k=4
for i in range(k):
    for j in range(len(arr)-1-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1]=arr[j+1], arr[j]
print(arr[k-1])