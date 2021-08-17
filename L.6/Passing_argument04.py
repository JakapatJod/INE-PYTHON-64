def reverse_name(first,last): #รับข้อมูลมาจาก reverse_name(first_name,last_name)
    print(last,first)

def main():
    first_name = input('Enter you first name: ')
    last_name = input('Enter your last name: ')
    print('Your name reversed is')
    reverse_name(first_name,last_name)

main()