total = 0
for x in range(2,10001):
    totalDivisors = 0
    for y in range(1,x):
        if x % y == 0:
            totalDivisors += y
    if totalDivisors == x:
        total += x
        print(x)
print(total)