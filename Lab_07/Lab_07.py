#Lab Sheet 07

#Question 1
'''
Bubble Sort is a popular sorting algorithm. It works by repeatedly swapping adjacent elements that 
are out of order.

BUBBLESORT(A)

1. for i = 1 to A.length – 1
2. for j = A.length downto i + 1
3. if A[j] < A[j – 1]
4. exchange A[j] with A[j – 1]

a) Read 8 numbers from the keyboard and store them in an array. Sort the numbers using 
the bubble sort algorithm.

b) Find out the time complexity of bubble sort in Big O Notation.
'''

A=[]
for v in range(8):
    A.append(input("Enter Number : "))
print(A)

#implementation of bubblesort
def bubbleSort(A):
    n =len(A)
    for i in range (0,n):
        for j in range(n-1,i,-1):
            if A[j]< A[j-1]:
                A[j],A[j-1] = A[j-1],A[j]

#call the bubblesort
bubbleSort(A)
print("Sorted Array : ")
print(A)
