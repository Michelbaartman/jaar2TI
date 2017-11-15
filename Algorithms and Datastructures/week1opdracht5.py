def iets(num):
    """
    wip
    """
    prev = ''
    count = 1
    counting = False
    endStr = ''
    numStr = str(num) + ' '
    for i in numStr:
        if i == prev:
            count += 1
        else:
            if counting == True:
                endStr += str(count) + prev
                counting = False
            count = 1
            prev = i
            counting = True


    return int(endStr)

num = 1133444111
print(num)
print(iets(num))