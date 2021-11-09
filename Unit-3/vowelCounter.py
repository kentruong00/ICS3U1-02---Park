word = input()
vowel =  0
for x in word:
    if x in 'aeiouAEIOU':
        vowel += 1
print(vowel)
