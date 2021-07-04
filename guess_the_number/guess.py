import random

def guess_the_number(number):
    random_number = random.randint(1, number)
    guess = 0
    while guess != random_number:
        guess = int(input(f'input a number between 0 an 100: '))
        if(guess < random_number):
            print(f'Sorry your guess is too low. Try again...')
        elif(guess > random_number):
            print(f'Sorry your guess is too high. Try again')
    print(f'Congratulations!! You guess the correct number which is {random_number}')

guess_the_number(100)