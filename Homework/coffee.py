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
        
            
            again = input('\t\tDo you want to again ? (Enter y for yes): ')
            
        MENU.close()

    
    except IOError :
        print('An error occured trying to read the file.') 
    except ValueError:
        print('Non-numeric data was found in the file.')
    except:
        print('An error occured.')

mainMENU()