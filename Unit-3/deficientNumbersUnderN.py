# Deficient Numbers Under N
# Ken Truong
# ICS3U1-02 - Park
# 10/29/2021
# Output all decficiant numbers under input N
num = int(input())
i = 1
while i < num:
    x = 1
    sumOfProperDivisors = 0
    while x < i:
        if i % x == 0:
            sumOfProperDivisors += x
        x += 1
    if sumOfProperDivisors < i:
            print(i)
    i += 1
