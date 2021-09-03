def Run():
        import colorama
        from colorama import Back , Fore , Style
        colorama.init(autoreset=True)
    
        MENU = open('menu.txt','r')
        
        print(MENU.readline(),end='')
        
        a = 1

        for i in MENU:
            temp = i.rsplit('\n')[0].split()
            print(str(a)+'.'+temp[0].replace('_','  ').ljust(26)+temp[1].ljust(6)+temp[2].ljust(6)+temp[3])
            a = a + 1
        
        MENU.close()

        total = 0.0

        again = 'y'
        while again == 'y':
            print('')

            print(Back.BLUE+'-'*70)

            print('')

            order = int(input(Fore.YELLOW+'\t\t\tPlease insert your order : '))
            size = input(Fore.YELLOW+'\t\t\tSelect size S , M , L: ').upper()
            
            if size == 'S':
                size = 'S'
                index = 1
            elif size == 'M':
                size = 'M'
                index = 2
            elif size == 'L':
                size = 'L'
                index = 3
            
            MENU = open('menu.txt', 'r')
            
            MENU.readline()
            MENU.readline()
            MENU.readline()
            
            a = 1
            
            for calculate in MENU:
                if order == a: 
                    temp = calculate.rsplit('\a')[0].split()
                    total += int(temp[index])
                a = a + 1
            print(Back.BLUE+'-'*70)
            print('')
            print(Fore.GREEN+"\t\t\tThis is the total : " + str(total) + "$")
            again = input(Fore.GREEN+'\t\tDo you want something more ? ( Enter y for yes ) : ')
            print('')
            print(Back.BLUE+'-'*70)
Run()