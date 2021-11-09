flag = True
contain = []
while flag:
    num = input('enter a number or type \'done\': ')
    if not 'done' in num:
        contain.append(int(num))
    else:
        flag = False
average = sum(contain)/len(contain)
print(average)
