#Fn = Fn-1 + Fn-2,


def Fibonacci(num):
    if num <= 1:
        return num

    return Fibonacci(num - 1) + Fibonacci(num - 2)


while True:
    #new line
    print("==========================")
    #get keyboard input
    n = int(input("Enter number: "))
    if n == -1:
        break

    #result
    result=(Fibonacci(n))
    print("Fibonacci Number is :" , str(result))
