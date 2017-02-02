def score(dice):
    if dice == []:
        return 0

    one = 100
    five = 50
    other_value = 100

    mydict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for num in dice:
        if num == 1:
            mydict[1] = mydict[1] + 1
        if num == 2:
            mydict[2] = mydict[2] + 1
        if num == 3:
            mydict[3] = mydict[3] + 1
        if num == 4:
            mydict[4] = mydict[4] + 1
        if num == 5:
            mydict[5] = mydict[5] + 1
        if num == 6:
            mydict[6] = mydict[6] + 1

    count_of_one = mydict[1] - 3
    count_of_five = mydict[5] - 3
    for k,v in mydict.iteritems():
        if k == 1 and v >= 3:
            one = 1000 + (count_of_one * 100)
        elif k == 1 and v < 3:
            one = mydict[1] * 100
        elif k == 5 and v >= 3:
            five = 500 + (count_of_five * 50)
        elif k == 5 and v < 3:
            five = mydict[5] * 50
        elif k != (1 | 5) and mydict[k] >= 3:
            other_value = mydict[k] * 100
        else:
                other_value = 0
    print one + five + other_value

score([1,1,1,2,2,2])
