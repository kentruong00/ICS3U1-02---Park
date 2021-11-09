iter = 1
total = 0
product = 1
nums = []
while iter <= 10:
    num = int(input())
    total += num
    product *= num
    nums.append(num)
print(total)
print(product)
print(sum(nums)/len(nums))
