inputs = 6
wins = 0
while inputs > 0:
    winLoss = input('W or L? ')
    inputs += -1
    if winLoss == 'W':
        wins += 1
    else:
        continue
if wins >= 5:
    print(1)
elif wins >= 3:
    print(2)
elif wins >= 1:
    print(1)
else:
    print(-1)