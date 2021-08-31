def mainMENU():
    try:    
        MENU = open('menu.txt','r')
        READ = MENU.read()
        print(READ)
    
        again = 'y'
        while again == 'y':
            print('')
            sell = int(input('Enter your number menu from 1,2,3,4,5,6 : '))
            print('')
        
            if sell == 1 :
                print('='*60)
                print('\t\t\tCaffe Latte','\nS = 110$','\tM = 125$','\tL = 140$')
                size1 = input('Enter you size : ')
                if size1 == 'S' :
                    print('')
                    print('\t\t\tSize S = 110$ ')
                    print('')
                elif size1 == 'M' :
                    print('')
                    print('\t\t\tSize M = 125$ ')
                    print('')
                elif size1 == 'L' :
                    print('')
                    print('\t\t\tSize L = 140$ ')
                    print('')
                else :
                    print('No option avaliable')
                print('='*60)

            elif sell == 2 :
                print('='*60)
                print('\t\tCappuccino','\nS = 110$','\tM = 125$','\tL = 140$')
                size2 = input('Enter you size : ')
                if size2 == 'S' :
                    print('')
                    print('\t\t\tSize S = 110$ ')
                    print('')
                elif size2 == 'M' :
                    print('')
                    print('\t\t\tSize M = 125$ ')
                    print('')
                elif size2 == 'L' :
                    print('')
                    print('\t\t\tSize L = 140$ ')
                    print('')
                else :
                    print('No option avaliable')
                print('='*60)

            elif sell == 3 :
                print('='*60)
                print('\t\tCaffe Mocha','\nS = 120$','\tM = 140$','\tL = 155$')
                size3 = input('Enter you size : ')
                if size3 == 'S' :
                    print('')
                    print('\t\t\tSize S = 120$ ')
                    print('')
                elif size3 == 'M' :
                    print('')
                    print('\t\t\tSize M = 140$ ')
                    print('')
                elif size3 == 'L' :
                    print('')
                    print('\t\t\tSize L = 155$ ')
                    print('')
                else :
                    print('No option avaliable')
                print('='*60)
            
            elif sell == 4 :
                print('='*60)
                print('\t\tCaramel Macchiato','\nS = 135$','\tM = 150$','\tL = 165$')
                size4 = input('Enter you size : ')
                if size4 == 'S' :
                    print('')
                    print('\t\t\tSize S = 135$ ')
                    print('')
                elif size4 == 'M' :
                    print('')
                    print('\t\t\tSize M = 150$ ')
                    print('')
                elif size4 == 'L' :
                    print('')
                    print('\t\t\tSize L = 165$ ')
                    print('')
                else :
                    print('No option avaliable')
                print('='*60)

            elif sell == 5 :
                print('='*60)
                print('\t\tWhite Chocolate Mocha','\nS = 135$','\tM = 150$','\tL = 165$')
                size5 = input('Enter you size : ')
                if size5 == 'S' :
                    print('')
                    print('\t\t\tSize S = 135$ ')
                    print('')
                elif size5 == 'M' :
                    print('')
                    print('\t\t\tSize M = 150$ ')
                    print('')
                elif size5 == 'L' :
                    print('')
                    print('\t\t\tSize L = 165$ ')
                    print('')
                else :
                    print('No option avaliable')
                print('='*60)

            elif sell == 6 :
                print('='*60)
                print('\t\tCaffe Americano','\nS = 100$','\tM = 115$','\tL = 130$')
                size6 = input('Enter you size : ')
                if size6 == 'S' :
                    print('')
                    print('\t\t\tSize S = 100$ ')
                    print('')
                elif size6 == 'M' :
                    print('')
                    print('\t\t\tSize M = 115$ ')
                    print('')
                elif size6 == 'L' :
                    print('')
                    print('\t\t\tSize L = 130$ ')
                    print('')
                else :
                    print('No option avaliable')
                print('='*60)

            else :
                print('\tNo option avaliable')
            
            again = input('\t\tDo you want to again ? (Enter y for yes):')
            
        MENU.close()

    
    except IOError :
        print('An error occured trying to read the file.') 
    except ValueError:
        print('Non-numeric data was found in the file.')
    except:
        print('An error occured.')

mainMENU()