print('--------------')
print('KPH \tMPH')
print('--------------')
for kph in range(60,131,10):
    mph = (kph*0.621) 
    print(kph,'\t', format(mph,',.1f'))
print('--------------')