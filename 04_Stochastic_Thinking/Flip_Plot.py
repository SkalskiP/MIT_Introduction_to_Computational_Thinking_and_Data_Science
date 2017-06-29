import random
import pylab

def flipPlot(minExp, maxExp):
    """Assumes minExp and maxExp positive integers: minExp < maxExp
    Plot results of 2**minExp to 2** maxExp coin flips"""
    ratios = []
    diffs = []
    xAxis = []
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        numHeads = 0
        for n in range(numFlips):
            if random.random() < 0.5:
                numHeads += 1
        numTails = numFlips - numHeads
        ratios.append(numHeads/float(numTails))
        diffs.append(abs(numHeads - numTails))
    pylab.title('Difference Between Heads and Tails')
    pylab.grid(True)
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Abs(#Heads - #Tails)')
    pylab.plot(xAxis, diffs, 'bo')
    pylab.xscale('log')
    pylab.yscale('log')
    pylab.savefig('heads_tails_difference.png')
    pylab.figure()
    pylab.grid(True)
    pylab.title('Heads/Tails Ratios')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('#Heads/#Tails')
    pylab.plot(xAxis, ratios, 'bo')
    pylab.xscale('log')
    pylab.savefig('heads_tails_ratio.png')

random.seed(0)
flipPlot(4, 20)