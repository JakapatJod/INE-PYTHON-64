def main():
    try:
        total = 0
        status = ''
        while(status.upper() != 'N'):
            infile = open('menu.txt', 'r')
            print(infile.readline(),end="")
            temp = infile.readline()
            print(temp.split()[0].ljust(28)+temp.split()[1].ljust(5)+temp.split()[2].ljust(7)+temp.split()[3])
            temp = infile.readline()
            print(temp.split()[0].rjust(33)+temp.split()[1].rjust(6)+temp.split()[2].rjust(6))

            n = 1
            for line in infile:
                temp = line.rsplit('\n')[0].split()
                print(str(n)+'.'+temp[0].replace('_',' ').ljust(26)+temp[1].ljust(6)+temp[2].ljust(6)+temp[3])
                n+=1
            infile.close()
            c = int(input('Plasea select number: '))
            s = input('Type T , G , V: ')
            if s.upper() == 'T':
                size = 'TALL(120z)'
                index = 1
            elif s.upper() == 'G':
                size = 'GRANDE(160z)'
                index = 2
            elif s.upper() == 'V':
                size = 'VENTI(200z)'
                index = 3

            infile = open('menu.txt', 'r')
            infile.readline()
            infile.readline()
            infile.readline()
            n = 1
            for line in infile:
                if c == n: 
                    temp = line.rsplit('\n')[0].split()
                    print("your select: " +temp[0]+'  '+size+'  '+temp[index])
                    total += float(temp[index])
                n+=1

            print('total =', total)
            status = input('Your have select again? (Y/N) : ')


    except Exception as err:
        print(err)
main()