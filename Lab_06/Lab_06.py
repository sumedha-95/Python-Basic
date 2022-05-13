#Lab 06
#Question 1
'''
a) Write a program to read a set of numbers (between 10 to 20) from the keyboard and store 
them in an array.

b) Sort the numbers in ascending order with the Insertion sorting algorithm.

c) Calculate how many times it executes the while of the algorithm.
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
