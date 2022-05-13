'''
a = input("Enter Charactor :")
b = ord(a)
print(b)

#in one line
print(ord(input("Enter Charactor :")))

print(chr(int(input("Enter ASCII Value :"))))

a = 'Hello'
len(a)

s = "Python"
s[0]
'''

'''
a=20
if (a==10):
    print("A is equal to 10")
    print("A is an integer")

elif a<50:
    print("A is less than 50")
    if a == 20:
        print("A is equal to 20")
        
else:
    print("A is not equal to 10")
'''

'''
#Exercise 01
a= int(input("Enter Number A: "))
b= int(input("Enter Number B: "))

if a>b:
    print("A is larger..")
elif b>a :
    print("B is larger..")
else:
    print("A and B are equal..")
'''

'''
#Exercise 02
a= int(input("Enter Number A: "))
b= int(input("Enter Number B: "))
c= int(input("Enter Number C: "))

if a<b and a<c :
    print(str(a)+"  is the minimum..");
elif b<a and b<c:
    print(str(b)+"  is the minimum..");
else :
    print(str(c)+"  is the minimum..");
'''

'''
#Exercise 03
a= int(input("Enter Number A: "))

x=a%2

if (x==0):
    print("A is Even Number...")
else:
    print("A is Odd Number...")

'''

'''
#Itaretions
for count in range(5):
    print("Hello")
'''

'''
for count in [0,1,2,3,4]:
    print("Hello")
    print("Good bye")

'''
'''
for count in range (1,7,2):
    print(count)
'''

'''
for count in range(4,1,-1):
    print(count)

'''

#Accumulator Loop
'''
total = 0
for n in range(1, 6):
   total = total + n
print(total)
'''

'''
for i in range(5):
    num= eval(input("Enter a number:"))
    print("The sequence of your number is ",num+num)
print("The Loop is now done.")
'''

'''
for i in range(7):
    for j in range(1,i+2):
        print(j,end="")
    print()
'''

'''
#while Loop
i=0
while i <10:
    print(i)
    i=i+1
'''

'''
#the braek statment
for i in range(10):
    num = eval(input("Enter Number :"))
    if num <0:
        break
'''


#Continue Statment
for i in [12,16,15,17,24,30]:
    if i % 5 == 1:
        continue
    print(i)
print("Done")



