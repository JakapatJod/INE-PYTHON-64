print('Multiply Table')
Ferrari = 'Y'    
while Ferrari == 'Y':    
    Toyota = int(input('Enter the first number = '))
    Ducati = int(input('Enter the second number = '))
    BMW = int(input('Enter the third number = '))
    print('')
    for Tesla in range(1,13):
        print(Toyota,'*',Tesla,'=',Toyota*Tesla,'\t',Ducati,'*',Tesla,'=',Ducati*Tesla,'\t',BMW,'*',Tesla,'=',BMW*Tesla)
    print('')
    Ferrari = input('Do you want to calculate again ? (Enter Y for yes): ')