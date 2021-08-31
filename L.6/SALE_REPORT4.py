def main():
    # Initialize an accmulator.
    total = 0.0

    try:
            # Open the sales_data.txt file
            infile = open('sales_data.txt','r')

            # Read the values from the file and
            # accumulate them
            for line in infile:
                amount = float(line)
                total += amount

            # Close the file.
            infile.close()

    except Exception as err:
        print(err)
        print('')
    else:
        # Print the total.
        print(format(total,'.2f'))
        print('')

# Call the main function.         
main()