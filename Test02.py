print('KPH \tMPH')
for kph in range(60,131):
    mph = (kph*0.621) 
    print(kph,'\t', format(mph,',.1f'))