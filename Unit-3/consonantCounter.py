word = input()
consonant =  0
for x in word:
    if not x in 'aeiou':
        consonant += 1
print(consonant)
