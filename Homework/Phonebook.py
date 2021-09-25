import pickle

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
    
        print('Please select operation Number !!','\n\t1.Show name and phone number.','\n\t2.Find phone number from name.',
        '\n\t3.Change the phone number you want.','\n\t4.Delete the phone number you want. ','\n\t5.Clear all.','\n\t6.Exit Program.')

        order = int(input("Select the number : "))
    
        if order == SHOW_NAME_PHONE :
            Openfile = open('PhoneNumber.dat','rb')
            read = pickle.load(Openfile)
            print('\t',read)
    
        elif order == FIND :
            FileName = input("Find phone number from name : ")
            Openfile = open('PhoneNumber.dat','rb')
            Enter_FIND = pickle.load(Openfile)
            if FileName in Enter_FIND:
                print('\t',Enter_FIND[FileName])
            else:
                print('No options available!!')
    
        elif order == CHANGE_THE_PHONE_NUMBER:
            FileName = input("Enter the name for find phone number: ")
            phoneNumber = input('Enter the phone number would like to change: ')
            Openfile = open('PhoneNumber.dat','wb')
            [FileName] = phoneNumber
        
        elif order == DELETE_PHONE_NUMBER: 
            FileName = input("Enter the name you want to delete. : ")
            Openfile = open('PhoneNumber.dat','wb')
            display_file = pickle.dump(PHONE,Openfile)
            del display_file[FileName]
            Openfile = open('PhoneNumber.dat','rb')
            display_file = pickle.load(PHONE,Openfile)
            print(display_file)
    
        elif order == CLEAR_ALL : 
            Openfile = open('PhoneNumber.dat','r+')
            display_file = pickle.dump(Openfile)
            del display_file[Openfile]
            print('after clear')
        
        elif order == EXIT_PROGRAM : 
            print('-'*50)
            print('\tExiting the program....')
            print('-'*50)
        
        else:
            print('No options available!!')
        
        Openfile.close()
main()