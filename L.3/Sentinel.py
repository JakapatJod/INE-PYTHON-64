keep_going = 'y'
while keep_going == 'y':
    sales = float(input("Enter the item's wholesale cost: "))
    commission = sales * 2.5
    print('Retail price: $',  \
    format(commission,',.2f'), sep='')
    keep_going = input('Do you have another'+ \
        'item? (Enter y for yes): ')
print('This End')

