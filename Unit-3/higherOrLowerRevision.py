from random import randrange
play = True
flag = bool
win = 0
loss = 0

while play:
    print('new round')
    gen1 = randrange(1,101)
    print(gen1)
    player = input()
    gen2 = randrange(1,101)
    print(gen2)
    
    if gen2 > gen1:
        condition = 'higher'
    else:
        condition = 'lower'

    if player == condition:
        print('correct!')
        win += 1
        print('streak:',win)
    else:
        win = 0
        print('wrong')
        loss += 1
        print('losses:',loss)

    if win == 5:
        play = False
        flag = True
    if loss == 5:
        play = False
        flag = False
if flag:
    print('player won')
else:
    print('player lost')
