a = int(input())
b = int(input())
c = int(input())
x = 0
flag = True
def f(x):
    return a*(x**2) + b*x + c
while x < 10:
    if f(x) == 0:
        print('y = 0 at:',x)
        flag = False
    if f(x) < 0 < f(x+1):
        print('y = 0 occurs between', x,'and', + x+1)
        flag = False
    if f(x) < 0 < f(x-1):
        print('y = 0 occurs between', x-1,'and', + x)
        flag = False
    x += 1
if flag:
    solution = 'none'
    print(solution)
    

        

