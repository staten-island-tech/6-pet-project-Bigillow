def gamble(quarter, one, two, three):
    x = one
    y = two
    z = three
    money = quarter
    stage = 1
    play = 0
    while money > 0:
        if stage == 1:
            money -= 1
            play += 1
            stage += 1 
            if x < 34:
                x += 1
            elif x == 34:
                x = 0
                money += 30
        elif stage == 2:
            money -= 1
            play += 1
            stage += 1
            if y < 99:
                y += 1
            elif y == 99:
                y = 0
                money += 60
        elif stage == 3:
            money -= 1
            play += 1
            stage = 1
            if z < 9:
                z += 1
            elif z == 9:
                z = 0
                money += 9

    print("Martha plays " + str(play) + " time before going broke.")
    
gamble(100000, 4, 9, 3)