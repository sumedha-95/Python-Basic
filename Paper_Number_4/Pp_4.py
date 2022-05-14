# Python3 program to calculate pow(x,n)

def power(x, n):

	if (n == 0) or (x == 1):return 1

	return x * power(x,n-1)

while True:
    print("============================")
    #Keyboard input
    x = int(input("Enter Number for X :"))
    n = int(input("Enter Number for n :"))
    if x == -1 or n == -1:
            break
        
    answer = (power(x, n))
    print("Power is :",str(answer))

