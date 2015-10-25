def fixedMonthly(balance,annualInterestRate):
    net_bal=balance
    monthly_payment=10

    while (net_bal>0):
        count =1
        net_bal=balance
        while(count<=12):
            net_bal=(net_bal-monthly_payment)*(1+annualInterestRate/12)
            count+=1
        monthly_payment+=10

    print("Lowest payment:"+" "+str(monthly_payment-10))    
