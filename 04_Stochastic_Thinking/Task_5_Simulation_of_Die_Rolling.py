import random

# IMPLEMENTING A RANDOM PROCESS

def rollDie():
    """returns a random int between 1 and 6"""
    return random.choice([1, 2, 3, 4, 5, 6])

def testRoll(n = 10):
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    print(result)

# A SIMULATION OF DIE ROLLING

def runSim(goal, numTrials, txt):
    """Our goal, for example: are we gonna get 5 ones
    numTrials: how many times we will roll die
    txt: text that will be printed in console, name of test"""

    # initialize variable that count number of times we reached goal
    total = 0
    # run test numTrials times
    for i in range(numTrials):
        result = ''
        # from the length of goal we know, how many times we need to roll die
        for j in range(len(goal)):
            result += str(rollDie())

        # we check the result, and if it has the property that we want
        # in this case it's equal to the goal than we increment the total
        if result == goal:
            total += 1
    print('Actual probability of', txt, '=', round(1/(6**len(goal)), 8))
    estProbability = round(total/numTrials, 8)
    print('Estimated Probability of', txt, '=', round(estProbability, 8))

runSim('11111', 100000, '11111')