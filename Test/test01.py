l = input('')
count ["UPPER": 0]
for i in l :
    if l.isupper():
        count['UPPER'] += 1
    else:
        pass

print("UPPER case letter count is : ",count["UPPER"])