flag = True
longestName = ''
longestNamelen = 0
while flag:
    name = input('enter a name or type \'done\': ')
    if not 'done' in name:
        if len(name) > longestNamelen:
            longestName = name
            longestNamelen = len(longestName)
    else:
        flag = False

print(longestName)
    
