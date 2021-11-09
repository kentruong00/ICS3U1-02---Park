sumOfProperDivisors = 0
i = int(input())
x = 0
while x < i:
    if i % x == 0:
        sumOfProperDivisors += x
        print(sumOfProperDivisors)
    x += 1
    print(x)
if sumOfProperDivisors < i:
        print('deficient')
else:
        print('abundant')