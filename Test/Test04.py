print('Multiply Table')
Ferrari = 'y'    
while Ferrari == 'y':    
    Toyota = int(input('\tEnter the first number = '))
    Ducati = Toyota + 1
    BMW = Toyota + 2
    print('-'*45)
    print('')
    for Tesla in range(1,13):
        print('|','\t',Toyota,'*',Tesla,'=',Toyota*Tesla,'\t','|','\t',Ducati,'*',Tesla,'=',Ducati*Tesla,'\t','|','\t',BMW,'*',Tesla,'=',BMW*Tesla,'\t','|')
    print('')
    print('-'*45)
    Ferrari = input('Do you want to calculate again ? (Enter y for yes): ')
