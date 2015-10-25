# 6.00 Problem Set 9

import numpy
import random
import pylab
from ps8b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    
    #simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol':False}, 0.005, numTrials, 0)   
    #simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol':False}, 0.005, numTrials, 75)   
    totNumVirusesT1 = simulationWithDrug(200, 2000, 0.1, 0.05, {'guttagonol':False}, 0.005, numTrials, 150)
    totNumVirusesT2 = simulationWithDrug(200, 2000, 0.1, 0.1, {'guttagonol':False}, 0.005, numTrials, 150)   
    #simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol':False}, 0.005, numTrials, 300)   
    pylab.subplot(221)
    pylab.hist(totNumVirusesT1, bins = 50)
    pylab.title('Histogram for trials')
    pylab.xlabel('Population')
    pylab.ylabel('Trials')
    pylab.xlim(min(totNumVirusesT1), max(totNumVirusesT1))
    #pylab.show()


    pylab.subplot(222)
    pylab.hist(totNumVirusesT2, bins = 50)
    pylab.title('Histogram for trials')
    pylab.xlabel('Population')
    pylab.ylabel('Trials')
    pylab.xlim(min(totNumVirusesT2), max(totNumVirusesT2))
    pylab.show()


#simulationDelayedTreatment(500)

#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    totNumVirusesT1 = simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol':False, 'grimpex':False}, 0.005, numTrials, 150, 0)
    totNumVirusesT2 = simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol':False, 'grimpex':False}, 0.005, numTrials, 150, 75)
    totNumVirusesT3 = simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol':False, 'grimpex':False}, 0.005, numTrials, 150, 150)
    totNumVirusesT4 = simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol':False, 'grimpex':False}, 0.005, numTrials, 150, 300)

    pylab.subplot(221)
    pylab.hist(totNumVirusesT1, bins = 500)
    pylab.title('Histogram -- Delay 0 for trials:' + str(numTrials))
    pylab.xlabel('Population')
    pylab.ylabel('No of Trials')
    pylab.xlim(0, max(totNumVirusesT1))
    #pylab.show()


    pylab.subplot(222)
    pylab.hist(totNumVirusesT2, bins = 500)
    pylab.title('Histogram -- Delay 75 for trials:' + str(numTrials))
    pylab.xlabel('Population')
    pylab.ylabel('Trials')
    pylab.xlim(0, max(totNumVirusesT2))

    pylab.subplot(223)
    pylab.hist(totNumVirusesT3, bins = 500)
    pylab.title('Histogram -- Delay 150 for trials:' + str(numTrials))
    pylab.xlabel('Population')
    pylab.ylabel('Trials')
    pylab.xlim(0, max(totNumVirusesT3))
    #pylab.show()


    pylab.subplot(224)
    pylab.hist(totNumVirusesT4, bins = 500)
    pylab.title('Histogram -- Delay 300 for trials:' + str(numTrials))
    pylab.xlabel('Population')
    pylab.ylabel('Trials')
    pylab.xlim(0, max(totNumVirusesT4))
    pylab.show()

    
simulationTwoDrugsDelayedTreatment(500)
