
def evaluatePoly(poly, x):
    value = 0
    count = 0
    for coeff in poly:
        value+= coeff*(x**(count))
        count+=1
    return round(value,1)  
