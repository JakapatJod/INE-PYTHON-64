def main():

    emp_file = open('employee.txt','r')

    line = emp_file.readline()
    
    line1 = emp_file.readline()
    line2 = emp_file.readline()
    line3 = emp_file.readline()
    line4 = emp_file.readline()
    line5 = emp_file.readline()
    line6 = emp_file.readline()
    line7 = emp_file.readline()
    line8 = emp_file.readline()
    line9 = emp_file.readline()
    
    print('Name :',line1)
    print('ID :',line2)
    print('Dept :',line3)
    print('Name :',line4)
    print('ID :',line5)
    print('Dept :',line6)
    print('Name :',line7)
    print('ID :',line8)
    print('Dept :',line9)

    emp_file.close()

main()