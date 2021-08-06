print('\t \t \t \t \t1-100')
columns = int(input('\t \t \t \t \tHow many columns ? = '))
z = 1
while columns <= 0 or columns > 100:
    print('\t \t \t \t \tERROR: The score cannot be negative or be 0')
    print('\t \t \t \t \tor greater than 100.')
    columns = int(input('\t \t \t \t \tTry again = '))
while z <= 100:
    for c in range(columns):
        print(z,end='\t')
        z = z + 1
        if z > 100:
            break   
    print('')