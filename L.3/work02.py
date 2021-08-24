#\t เว้นวรรค
print('--------------')
print('KPHw\tMPH')
print('--------------')
for kph in range(60,131,10):
    mph = (kph*0.621) 
    print(kph,'\t', format(mph,',.1f'))
print('--------------')