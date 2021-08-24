def main():
    # Open the employee.txt file for reading
    emp_file = open('employee.txt','r')

    # Read all the lines from the file.
    for line in emp_file:
        # Convert line to a float
        amount = (line)

        # Format and display the amount.
        print(amount)
    
    # Close the file.
    emp_file.close()

# Call the main function
main()