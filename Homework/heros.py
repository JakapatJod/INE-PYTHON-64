def main():
        RED = '\033[31m'
        YELLOW  = '\033[33m'
        MAGENTA = '\033[35m'
        BLUE    = '\033[34m'
        GREEN   = '\033[32m'

        HERO = ['Dr.strange','Cpt.MARVEL','Black widow','Superman']
        again = 'y'
        while again == 'y':
            print('')
            print(RED+'Please select operation Heroes !!')
            print(YELLOW+'\t1. Display Heroes','\n\t2. Add Heroes','\n\t3. insert Heroes',
            '\n\t4. Remove Heroes',
            '\n\t5.Display Sorted Herors(Ascending / Descending)')
            print('')
            print(BLUE+'-'*60)
            print('')
            op = int(input(MAGENTA+'Select operation form 1, 2, 3, 4 , 5: '))
            print('')
            print(BLUE+'-'*60)
            
            if op == 1 :
                print(HERO)
            elif op == 2 :
                nameHERO = input(GREEN+'Enter you name HERO : ')
                HERO.append(nameHERO)
                print(HERO)
            elif op == 3 :
                print('')
            elif op == 4 :
                print(HERO)
                print(RED+'\tDr.strange = " d " ','\tCpt.MARVEL = " c " ',
                   '\n\tBlack widow = " b " ', '\tSuperman = " s " ')
                RE = input('Who do you want to remove from the list? \n( Enter " d " ," c "," b "," s " ) : ')
                if RE == 'd':
                    HERO.remove('Dr.strange')
                    print(HERO)
                elif RE == 'c':
                    HERO.remove('Cpt.MARVEL')
                    print(HERO)
                elif RE == 'b':
                    HERO.remove('Black widow')
                    print(HERO)
                elif RE == 's':
                    HERO.remove('Superman')
                    print(HERO)
                else:
                    print('\tNo options available!!')
            elif op == 5 :
                AD = input(GREEN+'Select Ascending or Descending (Enter "a" or "d ") : ')
                if AD == 'a':
                    HERO.reverse()
                    print(HERO)
                elif AD == 'd':
                    HERO.sort()
                    print(HERO)
                else:
                    print(RED+'\tNo options available!!')
            else:
                print('No options available!!')
            print(BLUE+'-'*60)
            print('')
            again = input(GREEN+'Do you want again ? (Enter y for yes) : ')
            print('')
            print(BLUE+'-'*60)
main()