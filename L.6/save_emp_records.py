import os 

def main():
    os.rename('employeex.txt','employee05')
    # Get the number of employee records to create.
    num_emps = int(input('How mant employee records ' + \
                    'do you want to create ? '))
    
    # Open the file writting.
    emp_file = open('employeex.txt','w')

    # Get each employee's data and write it to
    # the file.
    for count in range(1,num_emps + 1):
        # Get the data for an employee.
        print('Enter data for employee #', count, sep='')
        name = input('Name: ')
        id_num = input('ID Number: ')
        dept = input('Department: ')
        
        # Write the data as a records to the file.
        emp_file.write(name + '\n')
        emp_file.write(id_num + '\n')
        emp_file.write(dept + '\n')
        
        # Display a blank line.
        print()

    # Close the file.
    emp_file.close()
    print('Employee records written to employee.txt.')

# Call the main function
main()