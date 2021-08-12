print('\t\t\t\tMultiply Table')
Ferrari = 'y'    
while Ferrari == 'y':    
    Toyota = int(input('\t\t\t\tEnter the number = '))
    Ducati = Toyota + 1
    BMW = Toyota + 2
    print('-'*80)
    print('')
    for Tesla in range(1,13):
        print('|','\t',Toyota,'*',Tesla,'=',Toyota*Tesla,'\t','|','\t'
        ,Ducati,'*',Tesla,'=',Ducati*Tesla,'\t','|','\t'
        ,BMW,'*',Tesla,'=',BMW*Tesla,'\t','|')
    print('')
    print('-'*80)
    Ferrari = input('Do you want to calculate again ? (Enter y for yes): ')
