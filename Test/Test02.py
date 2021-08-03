columns = int(input('How many columns ? : '))
bar = int(100/columns)
x = 1
for i in range(bar):
    for j in range(columns):
        print(x,end='\t')
        x = x + 1 
    print('')