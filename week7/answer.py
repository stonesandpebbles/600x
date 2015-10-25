import pylab

def producePlot(temps):
    """
    Produces a plot difference of temperature between each day.
    """
    differences = []
    days = []
    for i in range(1, len(temps)):
        differences.append(temps[i] - temps[i-1])
        days.append(i+1)
    pylab.plot(days, differences)
    pylab.title('Differences in July 2012 Temperatures in Boston')
    pylab.xlabel('Days')
    pylab.ylabel('Temperature Differences')
    pylab.show()

def loadData():
    inFile = open('julyTemps.txt')
    days = []
    highs = []
    lows = []
    for line in inFile:
        # split up line into fields by spaces
        fields = line.split(' ')
        # Ignore non-data lines
        if len(fields) != 3 or 'Boston' == fields[0] or 'Day' == fields[0]:
            continue
        # Know fields represents [day, high, low]
        days.append(int(fields[0]))
        highs.append(int(fields[1]))
        lows.append(int(fields[2]))
    return (days, highs, lows)
                

(days, highs, lows) = loadData()
producePlot(highs)
