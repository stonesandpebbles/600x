
import pylab
import numpy

def findOrder(xVals, yVals, accuracy = 1.0e-1):
    order = 1
    length = len(xVals)
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    coeff = []
    while True:
        
        coeff, res, x, y, z = pylab.polyfit(xVals, yVals, order, full = True)
        print res
        if (res[0] <= accuracy):
            break
            
        order += 1    
    return coeff


print findOrder([1, 2, 3, 4, 5], [2, 5, 10, 17, 26])
