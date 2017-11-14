"""gemaakt door michel baartman v2a"""

def getNumbers(s):
    """
    getNumbers(s : string)
    disects numbers from given string and returns each pair as a list.

    s : string
        given string that will be disected
    theList : list
        list in which we will return at the end
    saving : bool
        boolean to check if multiple numbers are detected to save them as a whole
    savedInt : string
        place in which we save our current detected int
    valid : string
        a string in which we use to check for numbers
    neg : bool
        a boolean to set whether the current int variable is negative or not

    return : list
        returns a list of numbers from given string
    """
    theList = []
    saving = False
    savedInt = ''
    valid = '1234567890'
    neg = False

    for c in s:
        if c in valid:
            savedInt += c
            saving = True
        elif c is '-':
            neg = True
        else:
            if saving == True:
                if neg == True:
                    savedInt = int(savedInt)*-1
                    neg = False
                theList.append(int(savedInt))
                savedInt = ''
                saving = False
    if saving == True:
        if neg == True:
            savedInt = int(savedInt)*-1
        theList.append(int(savedInt))

    return theList

a = 'een123zinijwqidj029392ijwdjq9owo'
b = 'een123zin45 6met-632meerdere+7777getallen'
c = '9d9j1289u2dj1298du1892je8912hj-9999999'

print(getNumbers(a))
print(getNumbers(b))
print(getNumbers(c))