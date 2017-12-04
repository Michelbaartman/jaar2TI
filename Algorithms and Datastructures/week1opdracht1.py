"""gemaakt door michel baartman v2a"""

def mymax(a):
    """
    mymax(a : list)
    returns highest int/float value in list a

    a : list
       a list that should contain int's & floats. returns a
       error message when it does not.

    return : int/float
        returns the highest number in the given list
    """
    assert len(a) > 0, "not a list"
    highest = a[0]
    for i in a:
        assert type(i) == int or type(i) == float, "wrong type in list"
        if i > highest:
            highest = i
    return highest

a = [1, 3, 5, 2, 4]
b = []
d = [0]
c = [100, 125, 99, 'paard', 0.42]

list = [a, b, c, d]
for i in list:
    try:
        print(mymax(i))
    except AssertionError:
        print('faulty list')