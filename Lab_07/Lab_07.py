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
    A.append(int(input("Enter Number : ")))
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



#Question 2
'''
Consider the selection sort algorithm given below. Selection sort algorithm sorts n numbers stored in 
array A by first finding the smallest element of A and exchanging it with the element in A[1]. Then 
find the second smallest element of A, and exchange it with A[2]. Continue in this manner for the 
first n - 1 elements of A.

 SELECTION-SORT(A)
1. n = A.length
2. for j = 1 to n − 1
3. smallest = j
4. for i = j + 1 to n
5. if A[i ] < A[smallest]
6. smallest = i
7. exchange A[ j ] with A[smallest]
Write a program to sort a set of numbers using selection sort algorithm
'''

B = []
for v in range(6):
    B.append(int(input('Enter a Number :')))
print(B)

#implementation of selectionSort
def selectionSort(B):
    n = len(B)
    for j in range (0,n-1):
        smallest = j
        for i in range (j+1,n):
            if B[i] < B[smallest]:
                smallest = i
        B[j],B[smallest] = B[smallest],B[j]

#call the selectionSort
selectionSort(B)
print("Sorted Array :")
print(B)
        
