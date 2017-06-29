import random
import math
random.seed(0)

# APPROXIMATING USING A SIMULATION

def sameDate(numPeople, numSame):
    """Two arguments, number of people in the group and the number of people that
    we ask if they have birthday the same day."""
    # I am assuming that every birthday is equally likely
    possibleDates = range(366)
    # Table that keeps track of number of people that are born each day
    birthdays = [0]*366
    # Single test
    for p in range(numPeople):
        birthDate = random.choice(possibleDates)
        birthdays[birthDate] += 1
    return max(birthdays) >= numSame

def birthdayProb(numPeople, numSame, numTrials):
    numHits = 0
    for t in range(numTrials):
        if sameDate(numPeople, numSame):
            numHits += 1
    return numHits / numTrials

# SCRIPT

for numPeople in [10, 20, 40, 100]:
    print('For', numPeople, 'est. prob. of a shared birthday is', birthdayProb(numPeople, 2, 10000))
    numerator = math.factorial(366)
    denom = (366**numPeople)*math.factorial(366-numPeople)
    print('Actual prob. for N = 100 =', 1 - numerator/denom)