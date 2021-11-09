a = int(input())
b = int(input())
c = int(input())
x = 0
flag = True

while x < 10:
    if a*(x**2) + b*x + c == 0:
        print('y = 0 at:',x)
        flag = False
    if a*(x**2) + b*x + c < 0 < a*(x+1)**2 + b*(x+1) + c:
        print('y = 0 between', x,'and', + x+1)
        flag = False
    if a*(x**2) + b*x + c < 0 < a*(x-1)**2 + b*(x-1) + c:
        print('y = 0 between', x-1,'and', + x)
        flag = False
    x += 1
if flag:
    solution = 'none'
    print(solution)
    

        

