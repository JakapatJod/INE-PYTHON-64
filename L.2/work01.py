score1 = int(input('Enter the score for test 1: '))
score2 = int(input('Enter the score for test 2: '))
score3 = int(input('Enter the score for test 3: '))
avg = (score1 + score2 + score3)/3
print('The average score is ',(avg))
if avg >95:
    print('Congratulations!')
    print('That is a great average!')