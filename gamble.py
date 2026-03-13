def gamble(quater, one, two, three):
    x = one
    y = two
    z = three
    money = quater
    stage = 1
    play = 0
    while money > 0:
        if stage == 1:
            if x < 34:
                money -= 1
                play += 1
                x += 1
                stage += 1
            elif x == 34:
                money -= 1
                play += 1
                stage += 1
                x = 0
                money += 30
        elif stage == 2:
            if y < 99:
                money -= 1
                play += 1
                y += 1
                stage += 1
            elif y == 99:
                money -= 1
                play += 1
                stage += 1
                y = 0
                money += 60
        elif stage == 3:
            if z < 9:
                money -= 1
                play += 1 
                z += 1
                stage += 1
            elif z == 9:
                money -= 1
                play += 1
                z = 0
                stage += 1
                money += 9

    print("Martha plays " + str(play) + " time before going broke.")
    
gamble(77, 4, 9, 3)