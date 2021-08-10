print('Multiply Table')
Ferrari = 'y'    
while Ferrari == 'y':    
    Toyota = int(input('\tEnter the first number = '))
    Ducati = int(input('\tEnter the second number = '))
    BMW = int(input('\tEnter the third number = '))
    print('')
    for Tesla in range(1,13):
        print(Toyota,'*',Tesla,'=',Toyota*Tesla,'\t',Ducati,'*',Tesla,'=',Ducati*Tesla,'\t',BMW,'*',Tesla,'=',BMW*Tesla)
    print('')
    Ferrari = input('Do you want to calculate again ? (Enter y for yes): ')