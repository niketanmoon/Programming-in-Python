# Geeks for geeks Problem
# Array Rotation

arr = [1,2,3,4,5,6,7]
n = len(arr)
d = int(input("How many elements you wanna shift left"))

for i in range(d):
    temp = arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1]=temp
print(arr)
