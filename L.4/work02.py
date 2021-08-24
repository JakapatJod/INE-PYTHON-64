l = input('Enter a string: ')
print('This is what I found about that string:')
if l.isalnum() :
    print('The string is alphanumberic')
    if l.islower() :
        print('The letters in the string are all lowercase.')
    elif l.isnumeric() :
        print('The string consists only digits')
    elif l.isupper() :
        print("The string's alphabetic character are all upper case")
    elif l.isalpha() :
        print("The string consists of only alphabetic characters ")
    elif l.isspace() :
        print('The string consists of only whitespace characters')
else :
    print('No option avaliable')