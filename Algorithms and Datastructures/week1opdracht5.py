
def lookandsay_convert(num):
    """
    lookandsay_convert(num : int)
        converts given int towards a written way of reading,
        rather then a mathmetical one.

    prev : string
        previous number
    count : int
        count to show how many times a previous number has repeated.
    counting : bool
        a bool to check whether the previous number is repeating.
    endStr : string
        string which will be returned at the end as an int.
        all countings are saved within
    numStr : string
        converted num to string for easier handling

    return : int
        returns converted int
    """
    prev = ''
    count = 1
    counting = False
    endStr = ''
    numStr = str(num) + ' '
    for i in numStr:
        if i == prev:
            count += 1
        else: ## niet transpirant, duidelijker, compacter, simpeler, denk pythonic
            if counting == True:
                endStr += str(count) + prev
                counting = False
            count = 1
            prev = i
            counting = True
            
    return int(endStr)

def lookandsay_sequence(num, amount):
    """
    lookandsay_sequence(num : int, amount : int)
        iterates with lookandsay_convert on given num for 
        amount times.

    pos : int
        current position in the iteration.
    lst : list
        list in which the numbers will be saved and 
        returned at the end.

    return : list
        returns a list of numbers.
    """
    pos = 0
    lst = [num]
    while pos <= amount:
        lst.append(lookandsay_convert(lst[pos]))
        pos += 1

    return lst

num = 1133444111
print(num)
num2 = lookandsay_convert(num)
print(num2)
print(lookandsay_sequence(4,10))