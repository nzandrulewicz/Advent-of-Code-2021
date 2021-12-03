# Advent of Code 2021
# Day 2: Dive
# Developed by: Nick Andrulewicz
# Started: December 2, 2021
# Time took part 1: 16 minutes 58 seconds
# Time took part 2: 7 minutes 38 seconds



# ============
# + Contents +
# ============



# + Code +
# Reading File
# Stringed Numbers to Integers
# Functions
## coursePattern()
# Initiating the function
# + Resources +



# ========
# + Code +
# ========



# Reading File
## Read all the elements from the file into a list
courseFile = open("Steps.txt", "r")
steps = courseFile.read()
steps = steps.split()
courseFile.close()

# Stringed Numbers to Integers
## Change all the numbers from a string to an integer
for index, element in enumerate(steps):
    if index % 2 != 0:
        steps[index] = int(steps[index])

# Functions
## coursePatter()
### Determines what direction the ship is going by X units and stores
    # the updated calculations
def coursePattern(pSteps):
    hor = 0
    dep = 0
    aim = 0

    # Because the list is alternating between strings and ints with strings
        # coming first, +1 is implemented (i.e. pSteps[i++1]) to update
        # the calculations appropriately.
    for i in range(len(pSteps)):
        if (pSteps[i] == "forward"):
            hor += (pSteps[i+1])
            dep = dep + (aim * pSteps[i+1])
        elif (pSteps[i] == "down"):
            aim += (pSteps[i+1])
        elif (pSteps[i] == "up"):
            aim -= (pSteps[i+1])

    answer = hor * dep
    print(answer)

# Initiating the function
coursePattern(steps)



# =============
# + Resources +
# =============



# How to access every other element in a list using a for-loop in Python
## https://www.kite.com/python/answers/how-to-access-every-other-element-in-a-list-using-a-for-loop-in-python
### Helped with changing all the stringed numbers into ints
