"""gemaakt door michel baartman v2a"""

def getPriems(i):
    """
    getPriems(i : int)
        returns prime numbers between 2 and i

    theList : list
        list of numbers, first filled with integers between 2 to i, then !primes are cut from
        this list.
    pos : int
        current number to be written to theList
    invalid : set
        set of values that that are not prime numbers in the sweep
    multi : int
        current multiplier in the sweep
    cur : int
        current int value in the sweep

    return : list
        returns a list of prime numbers
    """
    theList = []
    pos = 2
    while pos <= i:
        theList.append(pos)
        pos += 1

    invalid = set()
    pos = 2
    multi = 2
    cur = 0

    for n in theList[:]:
        while cur <= i and n not in invalid:
            if n >= 2:
                cur = n*multi
                if cur <= i and cur not in invalid:
                    invalid.add(cur)
                multi += 1
        multi = 2
        cur = 0

    for j in invalid:
        theList.remove(j)


    return theList

print(getPriems(30))
print(getPriems(1000))