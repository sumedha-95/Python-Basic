#Lab 06
#Question 1
'''
a) Write a program to read a set of numbers (between 10 to 20) from the keyboard and store 
them in an array.

b) Sort the numbers in ascending order with the Insertion sorting algorithm.

c) Calculate how many times it executes the while of the algorithm.
'''
'''
A = []
for v in range(10):
    A.append(input("Enter a Number : "))
print(A)

def insertSort(A):
    for j in range(1 ,len(A)):
        key = A[j]
        i = j-1
        while (i > 0 and A[i]>key):
            A[i+1]=A[i]
            i=i-1
        A[i+1]=key
        
insertSort(A)
print("Sorted Array ")
for k in range(len(A)):
      print(A[k])

'''

#Question 2
'''
a. Write a program to read a set of numbers and store them on an array.

b. Write function named as partition to divide the array into two parts according to the 
partition point. 
'''

arr=[]
for v in range(7):
    arr.append(input("Enter Number : "))
print(arr)

def partition(arr,low,high):
    i = (low-1)
    pivot = arr[high]
    for j in range(low ,high):
        if arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return(i+1)
def quickSort(arr,low,high):
    if low <high:
        q = partition(arr,low,high)
        quickSort(arr,low,q-1)
        quickSort(arr,q+1,high)
quickSort(arr,0,len(arr)-1)
print("Sorted Array :")
for i in range(len(arr)):
    print(arr[i])
