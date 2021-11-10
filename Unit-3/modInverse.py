x = int(input())
m = int(input())
inverse = ''
for n in range(m):
    if (x*n) % m == 1:
        inverse = n
if inverse:
    print(inverse)
else:
    print('no such integer')