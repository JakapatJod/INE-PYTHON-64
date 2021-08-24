import random

HEADS = 1
TAILS = 2 
TOSSER = 10

def main():
    for toss in range(TOSSER):
        if random.randint(HEADS, TAILS) ==  HEADS:
            print('Heads')
        else :
            print('Tails')
main()