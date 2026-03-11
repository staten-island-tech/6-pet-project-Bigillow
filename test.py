
def gamble(quarters, one, two, three):
    money = quarters * 0.25
    x = 35 - one
    y = 100 - two
    z = 10 - three
    stage = 1
    play = 1
    while money > 0:
        if stage == 1 and x != 0:
            money -= 0.25
            stage += 1
            x -= 1
            play += 1
        elif stage == 1 and x == 0:
            money -= 0.25
            stage += 1
            x = 35
            money = 30 * 0.25
            play += 1
        if stage == 2 and y != 0:
            money -= 0.25
            stage += 1
            y -= 1