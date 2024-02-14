
""" try:
    num = int(input("enter an integer: "))
    a = [5,6]
    print(a[num])
except ValueError:
    print("number entered is not an integer please enter integer")
except IndexError:
    print("index out of range please enter valid index")
else:
    print("integer accepted") """


try:
    i = int(input("enter a no: "))
    if i > 0:
        print(f"{i} is a positive no" )
    elif i==0:
        print(f"i equal to 0")
    else:
        print(f"{i} is negative no")
except ValueError:
    print("number entered is not an integer please enter integer")
else:
    print("valid integer inserted")
finally:
    print("code executed")


