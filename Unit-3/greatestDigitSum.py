greatestNum = 0
greatestSum = 0
int1 = int(input('enter lower bound: '))
int2 = int(input('enter upper bound: '))
for x in range (int1,int2+1):
    total = 0 
    for y in str(x):
        total += int(y)
    if total > greatestSum:
        greatestNum = x
        greatestSum = total
print(f'{greatestNum} has the greatest digit sum of {greatestSum}')
