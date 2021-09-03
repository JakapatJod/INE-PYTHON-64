def mainMENU():
    try:    
        MENU = open('menu.txt','r')
        READ = MENU.read()
        print(READ)
            
        MENU.close()

    
    except IOError :
        print('An error occured trying to read the file.') 
    except ValueError:
        print('Non-numeric data was found in the file.')
    except:
        print('An error occured.')


def Run():
    import colorama
    from colorama import Back , Fore , Style
    colorama.init(autoreset=True)
    cost = [110,125,150,110,125,150,120,140,155,
            135,150,165,135,150,165,100,115,130]
    
    total = 0.0
    
    
    again = 'y'
    while again == 'y':
        print('')
        mainMENU()
        
        print(Back.BLUE+'-'*70)
        print('')
        print(Fore.RED+'!! If you want a caffe latte size S, enter the number 2.'
            ,Fore.RED+'\nEx.Please insert your order : 2 ')
        print('')
        print(Back.BLUE+'-'*70)
        print('')
        order = int(input(Fore.YELLOW+'\t\t\tPlease insert your order : '))
        order = [int(a) for a in str(order)]
        for val in order:
            total = total + cost[val-1]
        print(Fore.GREEN+"\t\t\tThis is the total : " + str(total) + "$")
        again = input(Fore.MAGENTA+'\t\t\tDo you want something more ? ( Enter y for yes ) : ')
        print('')
        print(Back.BLUE+'-'*70)
Run()
