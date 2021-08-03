columns = int(input('How many columns ? : '))
b = int(100/columns)
o = 1
for d in range(b):
    for a in range(columns):
        print(o,end='\t')
        o = o + 1 
    print('')