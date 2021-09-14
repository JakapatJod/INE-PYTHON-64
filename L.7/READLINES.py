def main():
    infile = open('C:/Users/HP/Desktop/INE-PYTHON-64/List/cities.txt','r')
    # Read the contents of the into a list.
    cities = infile.readlines()

    infile.close()

    index = 0
    
    while index < len(cities):
        cities[index] = cities[index].rstrip('\n')
        index += 1
    
    print('')
    print(cities)
    print('')

main()