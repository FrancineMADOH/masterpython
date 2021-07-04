import random

def computer_guess(number):
    low = 1
    high = number
    result = ''
    while result != 'c':
        guess = random.randint(low, high)
        result = input(f'Is { guess } too high (H) too low (L) or correct (c)? ').lower()
        if(result == 'h'):
            high = guess - 1
        elif(result == 'l'):
            low = guess + 1
    print(f'Congratulations the computer did guess your number which is { guess }')

computer_guess(100)





























