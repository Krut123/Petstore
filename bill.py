##product = input("product name")
##qty = int(input("enter quantity"))
##rate = float(input("enter rate"))
##bill amt=qty*rate
##
##if Bill_amt<=2000:
##    print("No discount")
##    print("Final Bill amount : ", Bill_amt)
##elif 2001<=Bill_amt<=4000:
##    print("Bill amount Before discound", Bill_amt)
##    print("5% discount")
##    Bill_amt=Bill_amt-Bill_amt*0.05
##    print("Final Bill amount : ", Bill_amt)
##elif 4001<=Bill_amt<=6000:
##    print("Bill amount Before discound", Bill_amt)
##    print("10% discount")
##    Bill_amt=Bill_amt-Bill_amt*0.1
##    print("Final Bill amount : ", Bill_amt)    
##else:
##    print("Bill amount Before discound", Bill_amt)
##    print("15% discount")
##    Bill_amt=Bill_amt-Bill_amt*0.15
##    print("Final Bill amount : ", Bill_amt)


##Bikename= str(input("Enter name of bike"))
##cost_price=int(input("Enter Cost price of bike"))
##
##if cost_price>100000:
##    print("Cost of the bike ",cost_price)
##    cost_price=cost_price+cost_price*0.15
##    print("Cost of the bike after tax applied ",cost_price)
##elif 50000<=cost_price<=100000:
##    print("Cost of the bike ",cost_price)
##    cost_price=cost_price+cost_price*0.1
##    print("Cost of the bike after tax applied ",cost_price)
##else :
##    print("Cost of the bike ",cost_price)
##    cost_price=cost_price+cost_price*0.05
##    print("Cost of the bike after tax applied ",cost_price)




nationality = input("enter nationality")
income = float(input("enter income"))


if nationality=="Indian" or nationality=="indian" or nationality=="INDIAN" :
    print("No tax")
else:
    if income<300000:
        print(" No income  tax is applied ",income)
    elif 300000<=income<=500000:
         income=income+income*0.05
         print("income after tax is ",income)
    elif 500001<=income<=800000:
         income=income+income*0.1
         print("income after tax is ",income)
    elif 800001<=income<=1500000:
         income=income+income*0.15
         print("income after tax is ",income)



    
        


















    
