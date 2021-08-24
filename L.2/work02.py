hours = int(input('Enter the hours worked '))
payrate = int(input('Enter the hourly pay rate '))
if hours >40:
    money=((hours-40)*1.5)*payrate+(40*payrate)
    print(money)
else :
    money= hours*payrate
    print(money)