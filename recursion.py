""" def abc():

    print("hello")
    abc()

abc() """


""" def abc(limit,current=1):
    if current<= limit:
        print(f"hello {current}")
        abc(limit,current+1)
abc(15) """

""" def countdown(n):
    print(n)
    if n==1:
        return 1
    else:
        countdown(n-1)
countdown(10) """


def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(6))

def fibonachy(f):
    if f<=1:
        return f
    else:
        return(fibonachy(f-1)+ fibonachy(f-2))
fterms = 10
for i in range(fterms):
    print(fibonachy(i),end=" ")





    
 

