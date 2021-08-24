def main():
    #Open a file named philosophers.txt
    outfile = open('philosophers.txt','w')



    #Write the name of three philosophers
    #to the file.
    outfile.write('John Locke\n')
    outfile.write('David Hume\n') #\n การขึ้นบรรทัดใหม่
    outfile.write('Edmund Burke\n')
    #Close the file.
    outfile.close()


#Call the main function.
main()