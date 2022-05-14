#Paper Number 06
#IT20643218



def sumcube(n):
    if n ==1:
        return 1

    return n*n*n+sumcube(n-1)

while True:
    #Key Board input
    print("===============================")
    n = int(input("A Positive Integer n :"))
    if n == -1:
        break

    answer = (sumcube(n))
    print("The sum of the n cubes",str(answer)) 
