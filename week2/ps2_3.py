def bisection(balance,annualIntRate):
    
    lower_bound=balance/12.0

    upper_bound=(balance*((1+annualIntRate/12)**12))/12
    #print("upper=="+str(upper_bound))
    #print("lower=="+str(lower_bound))
    

    net_bal=0

    epsilon=0.01
    
    

    net_bal=balance


    while(abs(net_bal) > epsilon):

        net_bal=balance

        monthly_payment = (upper_bound+lower_bound)/2

        count=1
       # print("monthly pay"+str(monthly_payment))
        while(count<=12):

            net_bal=(net_bal-monthly_payment)*(1+annualIntRate/12)

            count+=1
       # print("net_bal=="+str(net_bal))
        if net_bal > 0:
            
            lower_bound = monthly_payment

        else:

            upper_bound = monthly_payment


    print("Lowest payment"+" "+ str(round(monthly_payment,2)))           
            
