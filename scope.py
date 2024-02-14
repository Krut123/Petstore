""" num = int(input("enter a no: "))
def mul(n):
    for i in range(1,21):
        print(num * i)
mul(num)


# global variable : outside the function
x = "wpw" # global
def func():
    print("Python is",x)
func()


# local variable : inside the function
x = "wpw" # global
def func():

    print("Python is",x)
func() """

#use of global keyword
def fun():
    global s
    s += "ABC"
    print(s)

s = "python is greate "
fun()
s = "PQR"
print(s)
fun()

def sum(*args):
    global sum,avg
    sum = 0
    for i in args:
        sum += i
    
    avg = sum / len(args)
    

sum(1,2,3,4,5)
print(f"sum is {sum}")
print(f"average is {avg}")

def add():
    pass;
def mul():
    pass
add()
mul()


def evenodd(x):
    '''this function prints if a number is even or odd'''
    if x % 2==0:
        print("even")
    else:
        print("odd")
        return "saqlain"
print(evenodd.__doc__)
print(evenodd(25))
