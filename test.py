
def gamble(quarters, one, two, three):
    money = quarters * 0.25
    x = 35 - one
    y = 100 - two
    z = 10 - three
    stage = 1
    play = 0
    while money > 0.25:
        if stage == 1 and x > 2 and money > 0:
            money -= 0.25
            stage += 1
            x -= 1
            play += 1
        elif stage == 1 and x == 1 and money > 0:
            money -= 0.25
            stage += 1
            x = 35
            money += 30 * 0.25
            play += 1
        if stage == 2 and y > 2 and money > 0:
            money -= 0.25
            stage += 1
            y -= 1
            play += 1
        elif stage == 2 and y == 1 and money > 0:
            money -= 0.25
            stage += 1
            y = 100
            money += 60 * 0.25
            play += 1
        if stage == 3 and z > 2 and money > 0:
            money -= 0.25
            stage = 1
            z -= 1
            play += 1
        elif stage == 3 and z == 1 and money > 0:
            money -= 0.25
            z = 10
            play += 1
            money += 9 * 0.25
    if money == 0:
        print("Martha plays " + str(play) + " time before going broke.")
    
    
    

gamble(77, 4, 9, 3)