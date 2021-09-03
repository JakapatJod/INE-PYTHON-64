menu =['Caffe Latte','Cappuccino','Caffe Mocha','Caramel Macchiato'
        ,'White Chocolate Mocha','Caffe Americano']
cost = [110,125,150,110,125,150,120,140,155,135,150,165,135,150,165,100,115,130]
    
    
total = 0.0

    
again = 'y'
while again == 'y':

    print('')
    order = int(input('Please insert your order : '))
    order = [int(a) for a in str(order)]
    for val in order:
        total = total + cost[val-1]
    print("This is the total : " + str(total) + "$")
    again = input('Do you want something more? : ')