def main():
    number = int(input('Enter a nonnegaive integer: '))
    
    fact = factorial(number)

    print('The factorial of',number,'is',fact)

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1) #4! = 4x3x2x1 , 5! = 5x4x3x2x1

main()