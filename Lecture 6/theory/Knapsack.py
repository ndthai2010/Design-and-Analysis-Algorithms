from time import process_time

class items(object):
    def __init__(self, name, value, volume):
        self.name = name
        self.value = value
        self.volume = volume

    def getValue(self):
        return self.value

    def getVolume(self):
        return self.volume

    def density(self):
        return (self.value) / (self.volume)

    def __str__(self):
        return self.name

def buildBag(names, values, volumes):
    bag = []

    for i in range(len(names)):
        bag.append(items(names[i], values[i], volumes[i]))

    return bag

def arrangeItem(items, maxVolume, keyFunction):
    itemsCopy = sorted(items, key=keyFunction, reverse=True)

    result = []
    totalValue = 0
    totalVolume = 0

    for i in range(len(items)):
        if (totalVolume + itemsCopy[i].getVolume() <= maxVolume):
            result.append(itemsCopy[i])
            totalValue = totalValue + itemsCopy[i].getValue()
            totalVolume = totalVolume + itemsCopy[i].getVolume()

    return (result, totalValue)

def main():
    itemList = ['camera', 'speaker', 'headphone', 'smartphone', 'pen', 'notebook']

    values = [30, 35, 50, 100, 10, 150]

    volumes = [10, 20, 15, 30, 5, 25]

    itemList = buildBag(itemList, values, volumes)

    maxVolume = 55

    taken, totValue = arrangeItem(itemList, maxVolume, items.density)

    start = process_time()
    print('Total value : ', totValue)

    for i in range(len(taken)):
        print('  ', taken[i])

    end = process_time()

    print("Time complexity for arranging items in bag is ", end - start, "(seconds)")

if __name__ == '__main__':
    main()