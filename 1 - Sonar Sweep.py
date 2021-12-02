# Advent of Code 2021
# Day 1: Sonar Sweep
# Developed by: Nick Andrulewicz
# Started: December 1, 2021



# ============
# + Contents +
# ============



# + Code +                          Line 26
# Reading Numbers                   Line 31
# String to Integer                 Line 38            
# Functions                         Line 43
## groupAndAdd()                    Line 44
## checkIncrease()                  Line 62
# Initiating the Function           Line 75
# + Resources +                     Line 81



# ========
# + Code +
# ========



# Reading Numbers
## Read all the numbers from the file into a list
numberFile = open("Depth Measurements.txt", "r")
depths = numberFile.read()
depths = depths.split()
numberFile.close()

# String to Integer
## Change all the numbers from a string to an integer
for i in range(len(depths)):
    depths[i] = int(depths[i])

# Functions
## groupAndAdd()
### Nests the numbers in groups of threes into one bigger list
### Adds the groups together individually and puts numbers in a seperate list
def groupAndAdd(pDepths):
    groupedNumbersList = []
    addedNumbers = []
    groupSize = 3

    # Organizes the numbers in threes (sliding window)
    for i in range(len(pDepths) - groupSize + 1):
        groupedNumbersList.append(pDepths[i: i + groupSize])

    # Adds the numbers in each group and puts them into a seperate list
    for i in range(len(groupedNumbersList)):
        addedNumbers.append(sum(groupedNumbersList[i]))

    checkIncrease(addedNumbers)

## checkIncrease()
### Compares each number to the next to check if it increases or not
def checkIncrease(pAddedNumbers):
    increaseCounter = 0

    # If the number next in the list is higher than the previous, increase + 1
    for i in range(len(pAddedNumbers[:-1])):
        if (pAddedNumbers[i] < pAddedNumbers[i+1]):
            increaseCounter += 1

    # Total ammount of increased values
    print(increaseCounter)

# Initiating the function
groupAndAdd(depths)



# =============
# + Resources +
# =============



# Rolloing or sliding window iterator?
## https://stackoverflow.com/questions/6822725/rolling-or-sliding-window-iterator
### Helped with organizing all the numbers in groups of threes using the sliding window technique
