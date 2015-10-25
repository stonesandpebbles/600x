
from ps8b_precompiled_27 import *

def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """

    viruses = []
    
    totNumViruses = [0 for x in range(300)]
    totResViruses = [0 for x in range(300)]
    for j in range(numTrials):
        viruses = []
        for i in range(numViruses):
            viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
        patient = TreatedPatient(viruses, maxPop)
        #totNumViruses = [0 for x in range(300)]
        #totNumViruses[0] += patient.update()
        for k in range(300):
            if k == 150:
                patient.addPrescription('guttagonol')
            totNumViruses[k] += patient.update()
            totResViruses[k] += patient.getResistPop(['guttagonol'])
            
    avgNumViruses = [totNumViruses[y]/float(numTrials) for y in range(300)]   
    avgResViruses = [totResViruses[z]/float(numTrials) for z in range(300)]
    print avgNumViruses
    print '-------------'
    print avgResViruses
    
    pylab.plot(avgNumViruses)
    pylab.plot(avgResViruses)
    pylab.title('Average result of many trials')
    pylab.xlabel('Time')
    pylab.ylabel('Average Number of viruses in patient')
    pylab.legend('Avg Number of Viruses') 
    pylab.show()
    
simulationWithDrug(1, 20, 1.0, 0.0, {"guttagonol": True}, 1.0, 5)
#simulationWithDrug(1, 10, 1.0, 0.0, {}, 1.0, 5)
