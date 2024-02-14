def student_info(name,age,marks,college="ITvedant"):
    print("name:{} \n age: {} \n marks: {} \n college: {}" .format(name,age,marks,college))

student_info("krutarth",20,95,"srk")
student_info("yash",25,80,"abc")
student_info("madhav",24,85,"xyz")

def sum(*args):
    sum = 0
    for i in args:
        sum += i
    print(f"sum is {sum}")
    avg = sum / len(args)
    print(f"average is {avg}")

sum(1,2,3,4,5)

def display(a,b,*args):
    print(type(args))
    print("a=",a,"b=",b,"args=",args)
display(1,2,3,4,5,6,7)

def displaykw(**kwargs):
    print(kwargs)

displaykw(english=90,maths=95,science=85)

# student finction name age marks of student and print details

def student(name,age,**marks):
    print(name,age,marks)
student("krutarth",age=20,english=50,maths=60,science=85)
