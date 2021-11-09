num = int(input())
factorial = 1
for x in range(num,0,-1):
    factorial *= x
print(f'{num} factorial is equal to {factorial}')