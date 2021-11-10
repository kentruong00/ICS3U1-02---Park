flag =  True

while flag:
    num = int(input())
    if not num == 0:
        peri = ''
        l = 0
        w = 0
        factor = []
        for x in range(1,num):
            if num % x == 0:
                factor.append(x)
        for y in factor:
            temp = 2*y + 2*(num/y)
            if peri:
                if temp < peri:
                    peri = temp
                    l = y
                    w = num/y
            else:
                peri = temp
                l = y
                w = num/y
        print(f'Minimum perimiter is {peri} with dimensions of {l}x{w}')
    else:
        flag = False