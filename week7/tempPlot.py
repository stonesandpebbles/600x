import pylab

def ReadTemp():
    inFile = open('julyTemps.txt','r')
    count = 0
    temp = []
    line = inFile.readline()
    count +=1
    while not line == '':
        
        if count > 6:
            separated = line.split(' ')
            temp.append((int(separated[1]), int(separated[2])))
        count += 1
        line = inFile.readline()
    #print temp
    tempDiff = []
    for i in range(len(temp)-1):
        tempDiff.append(temp[i+1][0] - temp[i][0])
    print tempDiff    
    pylab.figure(0)
    pylab.plot(range(2,32),tempDiff)
    pylab.title('Temp diff plot')    
    pylab.xlabel('Days')
    pylab.ylabel('Temp difference')
    
    #pylab.legend()
    pylab.show()
        
ReadTemp()
