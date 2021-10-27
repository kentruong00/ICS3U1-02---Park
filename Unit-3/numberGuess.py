num = ''
if input('is the number 50 or greater? ') == 'y':
    for i in range(5,11):
        if num != '':
            break
        elif input('does the number start with ' + str(i)+" ? ") == 'y':
            for x in range(10):
                if input('does the number end in '+str(x)+' ? ') == 'y':
                    num = str(i) + str(x)
                    print(num)
                    break
else:
    for i in range(5):
        if num != '':
            break
        elif input('does the number start with '+ str(i)+"? ") == 'y':
            for x in range(10):
                if input('does the number end in '+ str(x) +' ? ') == 'y':
                    num = str(i) + str(x)
                    print(num)
                    break
                    
