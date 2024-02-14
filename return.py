""" def greet():
    return "hello"
print(greet());

def sum(a,b):
    return a+b
print(sum(3,5))

def evenodd(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
print(evenodd(5))

def multi():
    return 1,2,True,'abc'
print(multi(),type(multi))

def createlist(n):
    return [i for i in range(1,n+1)]
print(createlist(15),type(createlist))

def marks():
    marks = {"english":80,"maths":90,}
    return marks.items()
print(marks()) """

""" def eo(num):
    for n in num:
        if n % 2==0:
            print(n,"is even")
        else:
            print(f"{n} is odd")

vals = [20,5,60,8,10,80]
eo(vals) """


vals = []

n =int(input("enter no of element: "))
for i in range(n):
    ele = int(input(f"enter {i+1} element:"))
    vals.append(ele)

n = input("enter comma seperated value")
vals = tuple(int(item) for item in n.split(","))
eo(vals);