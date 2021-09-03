def mainMENU():
    try:    
        MENU = open('menu.txt','r')
        READ = MENU.read().split()
        print(READ)
        
        total = 0
        
        caffeS = 110
        caffeM = 125
        caffeL = 140
        CappuccinoS = 110
        CappuccinoM = 125
        CappuccinoL = 140
        CaffeMochaS = 120
        CaffeMochaM = 140
        CaffeMochaL = 155
        CaramelMacchiatoS = 135
        CaramelMacchiatoM = 150
        CaramelMacchiatoL = 165
        WhiteChocolateMochaS = 135
        WhiteChocolateMochaM = 150
        WhiteChocolateMochaL = 165
        CaffeAmericanoS = 100
        CaffeAmericanoM = 115
        CaffeAmericanoM = 130

        again = 'y'
        while again == 'y':
            print('')
            sell = int(input('Enter your number menu from 1,2,3,4,5,6 : '))
            print('')
            
            if sell == 1:
                print('\t\t\tCaffe Latte','\nS = 110$','\tM = 125$','\tL = 140$')
                size1 = input('Enter you size : ')
                
                if size1 == 'S':
                    print('\t\t\tSize S = 110$ ')
                    pop = caffeS + total
                    print('\t\t\t',pop)
                elif size1 == 'M':
                    print('\t\t\tSize M = 125$ ')
                    pop = caffeM + total
                    print('\t\t\t',pop)
            
            
            
            else :
                print('\tNo option avaliable')
           


            again = input('\t\tDo you want to again ? (Enter y for yes): ')
            
        MENU.close()

    
    except IOError :
        print('An error occured trying to read the file.') 
    except ValueError:
        print('Non-numeric data was found in the file.')
    except:
        print('An error occured.')

mainMENU()


