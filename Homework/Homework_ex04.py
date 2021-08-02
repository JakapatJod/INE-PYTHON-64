print('Please select operation - ')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')
op = int(input('Select operation form 1, 2, 3, 4 : '))
number1 = int(input('Enter first number = '))
number2 = int(input('Enter second number = '))
if op == 1 :
    calculate =number1+number2
    print(number1,'+',number2 ,'=',(calculate))
elif op == 2 :
    calculate =number1-number2
    print(number1,'-',number2 ,'=',(calculate))
elif op ==3 :
    calculate =number1*number2
    print(number1,'*',number2 ,'=',(calculate))
elif op ==4 :
    calculate =number1/number2
    print(number1,'/',number2 ,'=',(calculate))
else:
    print('No options available!!')