import random

# Constrants for rows and columns.
ROWS = 3
COLS = 4

def main():
    # Create a two-dimensional list.
    valus = [[0,0,0,0],
             [0,0,0,0],
             [0,0,0,0]]
    
    # Fill the list with random numbers.
    for r in range(ROWS):
        for c in range(COLS):
            valus[r][c] = random.randint(1,100)

    # Display the random numbers.
    print(valus)

main()