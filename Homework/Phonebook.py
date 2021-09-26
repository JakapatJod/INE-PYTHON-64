import os
import pickle
RED = '\033[31m'
YELLOW  = '\033[33m'
MAGENTA = '\033[35m'
BLUE    = '\033[34m'
GREEN   = '\033[32m'

def main(): 
    PHONE = {'Gust':'0946192332','Earth':'0630688993','Deaw':'0956123020','Bell':'0927845184','Dan':'0613298526','Chalongrath':'0999165470'
    ,'Fern':'0623289157','Mac':'0820759182','Plam':'0963916108','Mic':'0809031245','Jane':'092-9907061','Bunnapon':'0638011033'
    ,'Wave':'0957083561','Min':'0969936296','Toon':'065-6267683'}

    Openfile = open('PhoneNumber.dat','wb')
    pickle.dump(PHONE,Openfile)
    
    SHOW_NAME_PHONE = 1
    FIND = 2
    CHANGE_THE_PHONE_NUMBER = 3
    DELETE_PHONE_NUMBER = 4
    CLEAR_ALL = 5
    EXIT_PROGRAM = 6
    
    order = 0
    
    while order != EXIT_PROGRAM :
        print(RED+'=-='*30)
        print('')
        
        print(GREEN+'Please select operation Number !!','\n\t1.Show name and phone number.','\n\t2.Find phone number from name.',
        '\n\t3.Change the phone number you want.','\n\t4.Remove the phone number you want from the name.. ','\n\t5.Clear all.','\n\t6.Exit Program.')
        
        print('')
        print(RED+'=-='*30)
        print('')
        order = int(input(YELLOW+'\tSelect the number : '))
    
        if order == SHOW_NAME_PHONE :
            Openfile = open('PhoneNumber.dat','rb')
            read = pickle.load(Openfile)
            print('')
            print(GREEN+'Show name and phone number : ',BLUE+'\t',read)
            print('')
    
        elif order == FIND :
            try:
                print('')
                FileName = input(GREEN+'Find phone number from name : ')
                Openfile = open('PhoneNumber.dat','rb')
                Enter_FIND = pickle.load(Openfile)
                if FileName in Enter_FIND:
                    print(BLUE+'\t',Enter_FIND[FileName])
                else:
                    print(RED+'No options available!!')
            except KeyError:
                print('')
                print(YELLOW+'-'*50)
                print('')
                print(RED+'ERROR !!!')
                print('')
                print(YELLOW+'-'*50)
                print('')
    
        elif order == CHANGE_THE_PHONE_NUMBER:
            try:
                FileName = input(GREEN+'\tEnter a name to change the phone number. : ')
                phoneNumber = input(GREEN+'\tEnter the phone number would like to change. : ')
                Openfile = open('PhoneNumber.dat','wb')
                pickle.dump(PHONE,Openfile)
                PHONE[FileName] = phoneNumber
                print('')
                print(BLUE+'',PHONE)
                print('')
            except KeyError:
                print('')
                print(YELLOW+'-'*50)
                print('')
                print(RED+'ERROR !!!')
                print('')
                print(YELLOW+'-'*50)
                print('')

        elif order == DELETE_PHONE_NUMBER: 
            try:
                Deletename = input(GREEN+'\tEnter your name for delete : ')
                Openfile = open('PhoneNumber.dat','wb')
                pickle.dump(PHONE,Openfile)
                del PHONE[Deletename]
                print(BLUE+'',PHONE)
            except KeyError:
                print('')
                print(YELLOW+'-'*50)
                print('')
                print(RED+'There is no key for this option.')
                print('')
                print(YELLOW+'-'*50)
                print('')
        elif order == CLEAR_ALL : 
            os.remove('./PhoneNumber.dat')
            open('PhoneNumber.dat', 'w').close()
            print('')
            print(YELLOW+'*'*50)
            print('')
            print(RED+'\tAll data deleted')
            print('')
            print(YELLOW+'*'*50)
            print('')

        elif order == EXIT_PROGRAM : 
            print(BLUE+'-'*50)
            print('')
            print(MAGENTA+'\tExiting the program....')
            print('')
            print(BLUE+'-'*50)

        
        else:
            print('No options available!!')
        
        Openfile.close()
main()