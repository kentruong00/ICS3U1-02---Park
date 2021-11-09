a = int(input())
b = int(input())
c = int(input())
x = 0
while x < 10:
    if a*(x**2) + b*x + c == 0:
        print('y = 0 at:',x)
    x += 1
