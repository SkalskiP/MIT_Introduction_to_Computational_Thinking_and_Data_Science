#CLASS REPRESENTATION OF OBJECTS IN MENU

class Food(object):
    def __init__(self, n, v , w):
        self.name = n
        self.value = v
        self.calories = w

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def density(self):
        return self.getValue()/self.getCost()

    def __str__(self):
        return self.name + ': <' + str(self.value) + ', ' + str(self.calories) + '>'

# FUNCTION RESPONSIBLE FOR BUILDING MENU

def buildMenu(names, values, calories):
    """names, values, calories lists of same length.
    name a list of strings
    values and calories lists of numbers
    returns list of Foods"""
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))

    return menu

#BODY OF MAXVAL

def maxVal(toConsider, avail):
    """Assumes toConsider a list of items, avail a weight
    Returns a tuple of the total value of a solution to 0/1 and the items of solution
    
    toConsider. Those items that nodes higher up in the tree (corresponding to earlier calls
    in the recursive call stack) have not yet considered
    
    avail. The amount of space still available"""

    if toConsider == [] or avail == 0:
        # if we don't have any other products to consider or we don't have any weight available
        # base of our recursion
        result =(0, ())
        # local variable "result" records best solution found so far

    elif toConsider[0].getCost() > avail:
        # we don't explore left branch - we can not afford to put this item in our backpack
        # explore right branch only
        result = maxVal(toConsider[1:], avail)
        # we slice of firs element of list

    else:
        nextItem = toConsider[0]
        # explore left brunch
        # what will happen if we take "nextItem"
        withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getCost())
        withVal += nextItem.getValue()
        # explore right brunch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        # choose better brunch

        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))

        else:
            result  = (withoutVal, withoutToTake)

    return result

# USING BRUT FORCE

def testMaxVal(foods, maxUnits, printItems = True):
    print('Use search tree to allocate', maxUnits, 'calories')
    val, taken = maxVal(foods, maxUnits)
    print('Total value of items =', val)
    if printItems:
        for item in taken:
            print('    ', item)

names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]
foods = buildMenu(names, values, calories)

testMaxVal(foods, 750)

#CODE TO TRY LARGER EXAMPLES

import random

def buildLargeMenu(numItems, maxVal, maxCost):
    items = []
    for i in range(numItems):
        items.append(Food(str(i), random.randint(1, maxVal), random.randint(1, maxCost)))
    return items

for numItems in (5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60):
    items = buildLargeMenu(numItems, 90, 250)
    testMaxVal(items, 750, False)