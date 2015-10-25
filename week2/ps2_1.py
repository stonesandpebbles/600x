def minimum(balance,annualInterestRate,monthlyPaymentRate):

    count=1
    total=0
    month_pay=0
    while(count<=12):
        print("Month:"+" "+str(count))
        month_pay=monthlyPaymentRate*balance
        balance=(balance-month_pay)*(1+annualInterestRate/12)
        total+=month_pay
        print("Minimum monthly payment:"+" "+str(round(month_pay,2)))
        print("Remaining balance:"+" "+str(round(balance,2)))
        count+=1

    print("Total paid:"+" "+str(round(total,2)))
    print("Remaining balance:"+" "+str(round(balance,2)))
