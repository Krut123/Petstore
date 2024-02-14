""" fact = 1
for i in range(1,6):
    fact*=i
print(fact)

n=int(input("Enter a number"))
fact =1 
for i in range(1,n+1):
    fact *=i # fact = fact*i 
print(str(n)+"! ",fact)


for i in range(1,21):
    if i % 2 ==0:
        print("i=",i,"is even")
    else:
        print("i=",i,"is odd")
         """


""" for i in range(1,51):
    if i % 3==0 and i % 5==0:
        print(i, "is divisible by 3 and 5")
    else:
        print(i, "is not divisible by 3 and 5") """


""" for i in range(1,5):
    n = int(input("enter no"))
    if i % 3==0 and i % 5==0:
        print(i, "is divisible by 3 and 5")
    else:
        print(i, "is not divisible by 3 and 5") """




""" for i in range(1,10):
    n = int(input("enter no"))

    if i % 2 ==0:
        print("i=",i,"is even")
    else:
        print("i=",i,"is odd") """
        


 for i in range(1,6):
    n = int(input("enter no"))
    if n%2==0:
        print(n,"is divisible by 2")
    if n%3==0:
        print(n,"is divisible by 3")
    if n%4==0:
        print(n,"is divisible by 4")
    if n%5==0:
        print(n,"is devisible by 5")
    if print("no is not divisible by 2,3,4,5")
        


""" name = input("enter your name: ")

for i in name:
    if i=='A' or i=='a' or i=='E' or i=='e' or\
       i=='I' or i=='i' or i=='O' or i=='o' or\
       i=='U' or i=='u':
        print(i,"is s vowel")
    else:
        print(i,"is a constant")
 """


a = int(input("enter 1st no: "))
b = int(input("enter 2nd no: "))

operators = input("enter operators")

if operators== "+":
    print("a+b= ",(a+b)),
elif operators== "-":
    print("a-b= ",(a-b))
elif operators== "*":
    print("a*b= ",(a*b))
elif operators== "/":
    print("a/b= ",(a/b))
else:
    print("invalid input")
