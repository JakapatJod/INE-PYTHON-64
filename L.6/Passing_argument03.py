def main():
    value = 99
    print('')
    print('The value is', value)
    change_me(value) 
    print('Back in main the value is',value)
    print('')
#value = 99 ----------> arg = 99
def change_me(arg):
    print('I am changing the value')
    arg = 0
    print('Now the value is',arg)

main()