play = True
place = 1
snakeTop = [54,90,99]
snakeBot = [19,48,77]
ladderBot = [9,40,67]
ladderTop = [34,64,86]
while play:
    roll = int(input())
    if not roll == 0:
        if place + roll < 100:
            place += roll
            if place in snakeTop:
                place = snakeBot[snakeTop.index(place)]
            if place in ladderBot:
                place = ladderTop[ladderBot.index(place)]
            print('you are on square',place)
        elif place + roll == 100:
            place += roll
            print('you are on square',place)            
            print('You Win!')
        else:
            print('cannot advance')
            print('you are on square',place)
    else:
        play = False