import matplotlib.pyplot as plt

def main():

    left_edges = [0,10,20,30,40]

    heights = [100,200,300,400,500]

    bar_width = 10

    plt.bar(left_edges,heights,bar_width,color=('r','g','b','w','k'))
    
    plt.title('Sales by Year')

    plt.xlabel('Year')
    plt.ylabel('Sales')

    plt.xticks([0,1,2,3,4],
                ['2016','2017','2018','2019','2020'])
    plt.yticks([0,1,2,3,4,5],
                ['$0m','$1m','$2m','$3m','$4m','$5m'])

    plt.grid(True)

    plt.show()

main()