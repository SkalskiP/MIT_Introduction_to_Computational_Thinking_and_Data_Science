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

#BODY OF MAXVAL

def maxVal(toConsider, avail):
    """Assumes toConsider a list of items, avail a weight
    Returns a tuple of the total value of a solution to 0/1 and the items of solution
    
    toConsider. Those items that nodes higher up in the tree (corresponding to earlier calls
    in the recursive call stack) have not yet considered
    
    avail. The amount of space still available"""

    if toConsider == [] or avail == 0:
        # if we don't have any other products to consider or we don't have any space available
        result =(0, ())

    elif toConsider[0].getUnits() > avail:
        result = maxVal(toConsider[1:], avail)

    else:
        nextItem = toConsider[0]
        withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getUnits())
