
while True:
    num1 = int(input("enter first no: "))
    num2 = int(input("enter second no: "))
    operation = int(input('''what operation do you want to perform
                            1.addition
                            2.sub
                            3.multi
                            4.divi
                            5.mod
                            6.check even or odd
                            7.exit
                            ''' ))

    if operation ==1:
        print("add in",num1+num2)
    elif operation == 2:
        print("sub in",num1-num2)
    elif operation == 3:
        print("multi is",num1*num2)
    elif operation == 4:
        print("divi is",num1/num2)
    elif operation == 5:
        print("mod is",num1%num2)
    elif operation == 6:
        if num1 % 2 == 0:
            print("even")
        else:
            print("odd")
    elif operation == 7:
        break
    else:
        print("wrong input")

    