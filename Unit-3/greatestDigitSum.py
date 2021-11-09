greatestNum = 0
greatestSum = 0
for x in range (10,21):
    total = 0 
    for y in str(x):
        total += int(y)
    if total > greatestSum:
        greatestNum = x
        greatestSum = total
print(f'{greatestNum} has the greatest digit sum of {greatestSum}')
