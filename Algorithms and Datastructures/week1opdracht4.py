"""gemaakt door michel baartman v2a"""
import random

def classCreator(i):
    """
    classGenerator(i : int)
        creates a list with i amount integers, randomized between 1 and 365

    thisClass : list
        a list in which the integers will be saved
    j : int
        current location of appending

    return : list
        returns a list of integers
    """
    thisClass = []
    j = 0
    while j < i:
        thisClass.append(random.randrange(1, 365)) ## [ methode + for i in range ] comprehensive lists in python
        j += 1

    return thisClass

def classesCreator(i):
    """
    classesGenerator(i : int)
        creates a i amount of lists of classes

    theseClasses : list
        list of classes
    j : int
        current location of appending

    return : list
        returns a list of lists
    """
    theseClasses = []
    j = 0
    while j < i:
        theseClasses.append(classCreator(23))
        j += 1
    
    return theseClasses

def classCompare(lst, perBool):
    """
    classesGenerator(i : int, perBool : bool)
        compares a list of lists of numbers and returns the amount of repeating numbers
        contained in each list. if perBool is set to true, returns a percentage instead of amount

    doublesCheck : int
        starts at 0, counts upward based on how many repeating numbers in the given lists.
    pos1 : int
        position of the first interval
    pos2 : int
        position of the second interval
    students : int
        amount of students in total in all classrooms

    return : int
        returns doublesChecck
    """
    doublesCheck = 0
    pos1 = 0
    pos2 = 1
    students = 0
    for group in lst:
        for member in group:
            students += 1

    for list in lst:
        while pos1 < len(list): ## maak er een set van en vergelijk de set met aantal studenten
            while pos2 < len(list):
                if list[pos1] == list[pos2]:
                    doublesCheck += 1
                pos2 += 1
            pos1 += 1
            pos2 = pos1+1
        pos1 = 0
        pos2 = 1

    if not perBool:
        return doublesCheck
    if perBool:
        return int(doublesCheck / students * 100)

print(str(classCompare(classesCreator(1000), True))+'%, percentage check') ## 3% is niet goed, verjaardagsparadox
print(classCompare(classesCreator(1000), False))

