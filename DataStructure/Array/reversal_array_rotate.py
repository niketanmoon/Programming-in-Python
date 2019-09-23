"""
This is a GeekForGeeks Problem on Array Rotaion using Reversal
Here's the link to the problem:
geeksforgeeks.org/program-for-array-rotation-continued-reversal-algorithm/


"""
#Function for reversing. This is the main logic
def reverseArray(arr,s,e):
    while s<e:
        temp = arr[s]
        arr[s] = arr[e]
        arr[e] = temp
        s = s+1
        e= e-1

#Funcrion to call reverse functions in algorithmic steps
def rotate(arr,d):
    #corner cases: if shift is 0 then simply return
    if d == 0:
        return
    #1.Reverse the array from start to d
    reverseArray(arr,0,d-1)
    #2.Reverse the array from d+1 to n
    reverseArray(arr,d,n-1)
    #3.Reverse now the whole Array
    reverseArray(arr,0,n-1)
# Standard Input
arr = [1,2,3,4,5,6,7]
n = len(arr)
d = int(input("Enter how many shifts you wanna do: "))
#If the shifts are greater than array length
d = d % n

#Function call to rotate
rotate(arr,d)

#Printing the array
for i in range(n):
    print(arr[i],end=" ")
