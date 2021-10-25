i = 1
while i <= 50:
    output = ''
    if i % 3 == 0:
        output += 'Fizz'
    if i % 5 == 0:
        output += 'Buzz'
    if output == '':
        output = str(i)
    i += 1
    print(output)
