def main():
    #Open a file name philosophers.txt
    infile = open('philosophers.txt','r')

    #Read the file's contents. 
    file_contents = infile.read()

    infile.close()

    
    print(file_contents)

main()