print('\t \t \t \t \t1-100')
columns = int(input('\t \t \t \t \tHow many columns = '))
z = 1
while (z <= 100):
    for c in range(columns):
        print(z,end='\t')
        z = z + 1
        if z > 100:
            break
    print('')