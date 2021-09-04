def Run():
    try:
        import colorama
        from colorama import Back , Fore , Style
        colorama.init(autoreset=True)
    
        MENU = open('menu.txt','r')
        
        print(MENU.readline(),end='')
        
        custom = MENU.readline()
        
        print(custom.split()[0].rjust(0)+custom.split()[1].rjust(22)
        +custom.split()[2].rjust(6)+custom.split()[3].rjust(6))
    
        a = 1

        for i in MENU:
            custom = i.rsplit('\n')[0].split()
            print(str(a)+'.'+custom[0].replace('_',' ').ljust(26)
            +custom[1].ljust(6)+custom[2].ljust(6)+custom[3])
            
            a = a + 1
        
        MENU.close()

        SUM = 0.0

        again = 'y'
        while again == 'y':
            print('')

            print(Back.BLUE+'-'*70)

            print('')

            order = int(input(Fore.YELLOW+'\t\t\tSelect a menu from the top. : '))
            scale = input(Fore.YELLOW+'\t\t\tChoose size S , M , L : ').upper()
            
            print('')

            if scale == 'S':
                size = 'S'
                index = 1
            elif scale == 'M':
                size = 'M'
                index = 2
            elif scale == 'L':
                size = 'L'
                index = 3
            
            MENU = open('menu.txt', 'r')
            
            MENU.readline()
            MENU.readline()
            
            a = 1
            
            for calculate in MENU:
                if order == a: 
                    custom = calculate.rsplit('\a')[0].split()
                    SUM += int(custom[index])
                a = a + 1
            print(Back.BLUE+'-'*70)
            print('')
            print(Fore.GREEN+"\t\t\tThis is the SUM : " + str(SUM) + "$")
            again = input(Fore.GREEN+'\t\tDo you want something more ? ( Enter y for yes ) : ')
            print('')
            print(Back.BLUE+'-'*70)
    except IOError :
        print(Back.RED+'-'*70)
        print('')
        print(Fore.GREEN+'\t\tAn error occured trying to read the file.')
        print('')
        print(Back.RED+'-'*70)
    except ValueError:
        print(Back.RED+'-'*70)
        print('')
        print(Fore.GREEN+'\t\tNon-numeric data was found in the file.')
        print('')
        print(Back.RED+'-'*70)
    except:
        print(Back.RED+'-'*70)
        print('')
        print(Fore.GREEN+'\t\tAn error occured.')
        print('')
        print(Back.RED+'-'*70)

Run()