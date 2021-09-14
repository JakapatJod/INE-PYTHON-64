def main():

    cities = ['New York','Boston','Atlanta','Dallas']

    outfile = open('C:/Users/HP/Desktop/INE-PYTHON-64/List/cities.txt','w')
    cities = map(lambda x: x+'\n',cities)
    outfile.writelines(cities)

    outfile.close()

main()