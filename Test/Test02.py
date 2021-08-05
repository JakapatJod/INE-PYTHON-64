print('1-100')
columns = int(input('How many columns ? : '))
b = int(100/columns)
p = 1
for x in range(b):
    for c in range(columns):
        print(p,end='\t')
        p += 1
    print('')