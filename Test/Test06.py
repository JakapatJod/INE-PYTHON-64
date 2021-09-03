def show_item():
    MENUcaffe = [["1", "Caffe Latte", 110,125,150],
            ["2", "Cappuccino", 110,125,150],
            ["3", "Caffe Mocha ",120,140,155],
            ["4", "Caramel Macchiato  ", 135,150,165],
            ["5", "White Chocolate Mocha", 135,150,165],
            ["6", "Caffe Americano", 100,115,130]]
    print("\n")
    print("{: ^5} {: ^25} {: ^10} {: ^10} {: ^10}".format("Code", "Item","S","M","L"))
    for item in MENUcaffe:
        print("{: ^5} {: ^25} {: ^10} {: ^10} {: ^10}".format(*item))