print('1-100')
columns = int(input('How many columms ? = '))
for a in range(columns):
    for i in range(1,columns+1,1):
        if a == i:
            break
        print('',i,end='') 
    print("")