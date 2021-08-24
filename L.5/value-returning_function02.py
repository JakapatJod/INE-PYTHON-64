def get_name():
    first = input('Enter you first name: ')
    last = input('Enter your last name: ')
    #Return both name. ส่งคืนทั้งสองชื่อ
    return first, last

first_name,last_name = get_name() #สร้างตัวแปร ชื่อว่า first_name กับ last_name
print('First name: ',first_name,'Last name: ',last_name)