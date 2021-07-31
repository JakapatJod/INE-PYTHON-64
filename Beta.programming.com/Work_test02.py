sc1 = int(input(''))
sc2 = int(input(''))
sc3 = int(input(''))
cal = sc1+sc2+sc3
if cal >=80 :
    print('A')
elif cal >=75 :
    print('B+')
elif cal >=70 :
    print('B')
elif cal >=65 :
    print('C+')
elif cal >=60 :
    print('C')
elif cal >=55 :
    print('D+')
elif cal >=50 :
    print('D')
elif cal >=0 :
    print('F')
else :
    print('No option')