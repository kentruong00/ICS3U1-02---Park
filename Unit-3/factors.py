flag = True
while flag:
    num = int(input())
    if num > 0 :
        flag = False
        for x in range(1,num+1):
            if num % x == 0:
                print(x)
    else:
        print('invalid input')
            