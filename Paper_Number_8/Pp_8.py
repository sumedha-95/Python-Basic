#Paper Number 8
#IT20643218

def NumberSum(n):
    if n == 1:
        return 1

    return n + NumberSum(n-1)

#while loop
while True:
    print("===============================")
    #key board input
    n = int(input("A Positive Intiger n :"))
    if n == -1:
        break
    #answer
    Answer =(NumberSum(n))
    print("The Sum of the numbers",str(Answer))
