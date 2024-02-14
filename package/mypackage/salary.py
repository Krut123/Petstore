def calsal():
    basic = float(input("enter the basic salary"))
    da = 0.4 * basic
    hra = 0.3 * basic
    total_sal = basic + da + hra
    print("DA = ",da, "Hra = ",hra,"Gross salary = ",total_sal)
    