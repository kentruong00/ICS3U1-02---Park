flag = True
num = input()
oriNum = num
step = 0
while flag:
    if len(str(num)) == 1:
        flag = False
    else:
        total = 0
        step += 1
        inter = ''
        for x in str(num):
            total += int(x)
            inter += ' ' + x + ' ' + '+'
        print(f'Digit sum of {num} ={inter[:-1]}= {total}')
        num = total
print(f'Therefore {oriNum} takes {step} steps')