def main():
    # Open the employee.txt file for reading
    emp_file = open('employee.txt','r')
    STR = ['NAME : ','ID : ','Dept : ']
    
    n = 0
    
    for tes in emp_file :
        print(STR[n], tes.rstrip('\n')) 
        n = n + 1
        if n > 2:
            n = 0
    # Close the file.
    emp_file.close()

# Call the main function
main()