from random import randint
# generate a number 1 to 10
answer = randint(1, 10)
# ger input from user
# check that input is a number 1 -10
while True:
    try:
        guess = int(input('Guess a number from 1 to 10:  '))
        if 0 < guess < 11:
            if guess == answer:
                print('You are a genuis')
                break
        else:
            print('Hey, the number must be from 1 to 10')
    except ValueError:
        print('Please entre an number')
        continue   
# check if number is the right guess. Otherwise ask again 
