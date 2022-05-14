#Question 1
'''
Binary search algorithm finds the position of a target value within a sorted array. It is a divide and 
conquer search algorithm.
Algorithms compares the target value with the value of the middle element of the array. If they are 
equal, algorithm returns the middle position and search ends. If the target value is less than the 
middle element value, search continues on the lower half of the array. If the target value is greater 
than the middle element value, search continues on the upper half of the array. This process 
continues, eliminating half of the elements until the value is found or the array is exhausted. 
 BINARY-SEARCH(A, min, max, key)
1. if max < min
2. return false
3. else
4. mid =  (min + max)/2 
5. if A[mid] > key
6. return BINARY-SEARCH(A, min, mid-1, key)
7. else if A[mid] < key
8. return BINARY-SEARCH(A, mid+1, max, key)
9. else
10. return mid
Write a program to read sorted numbers and store them in an array. Search a given numbers using 
binary search algorithm.
'''

#arr = Array
#low = Start_Index
#high = End_Index
#x = Search Value
#mid = Mid_Index

arr =[]
for v in range(4):
    arr.append(int(input("Enter a Number :")))
print(arr)

x = int(input("Enter the Search Value :"))

def binary_search (arr ,low , high , x):

    #Check base case
    if high >= low:

        mid = (high + low)//2
        
        if arr[mid] ==x:
            return mid
        
        elif arr[mid] > x:
            return binary_search(arr ,low ,mid-1 ,x )
        
        else:
            return binary_search(arr ,mid+1 ,high ,x)
    else:
        return -1
    
#Function call
result = binary_search(arr , 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
