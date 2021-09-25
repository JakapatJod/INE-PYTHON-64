import pickle
def main():
    phone = {'Gust':'0946192332','Earth':'0630688993','Deaw':'095-6123020','Bell':'0927845184','Dan':'0613298526','Chalongrath':'099-9165470'
    ,'Fern':'062-3289157','Mac':'082-0759182','Plam':'096-3916108','Mic':'0809031245','Jane':'092-9907061','Bunnapon':'0638011033','Wave':'0957083561',
    'Min':'096-9936296','Toon':'065-6267683'}

    Openfile = open('PhoneNumber.dat','wb')
    
    Openfile.close()
    
    again = 'y'
    
    while again == 'y' :
        print('Please select operation Number !!','\n\t1.Show all of the user and phone number','\n\t2.Find phone number from name',
        '\n\t3.Fix phone number from name','\n\t4.Delete phone number from name ','\n\t5.Clear all of the information ')

        order = int(input("Select the number: "))
    
        if order == 1 :
            input_file = open('PhoneNumber.dat','rb')
            read = pickle.load(input_file)
            print(read)
    
        elif order == 2 :
            FileName = input("Enter the name for find phone number: ")
            input_file = open('PhoneNumber.dat','rb')
            display_file = pickle.load(input_file)
            if FileName in display_file:
                print(display_file[FileName]) 
    
        elif order == 3:
            input_file = open('PhoneNumber.dat','wb')
            FileName = input("Enter the name for find phone number: ")
            phone = input('Enter the phone number would like to change: ')
            [FileName] = phone
        
        elif order == 4: 
            FileName = input("Enter the name for delete user: ")
            input_file = open('PhoneNumber.dat','wb')
            display_file = pickle.dump(input_file)
            del display_file[FileName]
            input_file = open('PhoneNumber.dat','rb')
            display_file = pickle.load(input_file)
            print(display_file)
    
        elif order == 5 : 
            input_file = open('Phone.dat01','wb')
            display_file = pickle.dump(input_file)
            del display_file[input_file]
            print('after clear')
        
        else:
            print('No options available!!')
        
        again = input('Do you want again ? (Enter y for yes) : ')
main()