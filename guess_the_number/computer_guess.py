import random

def computer_guess(number):
    low = 1
    high = number
    result = ''
    while result != 'c':
        if low != high:
          guess = random.randint(low, high)
        else:
            guess = low
        result = input(f'Is { guess } too high (H) too low (L) or correct (c)? ').lower()
        if(result == 'h'):
            high = guess - 1
        elif(result == 'l'):
            low = guess + 1
    print(f'Congratulations the computer did guess your number which is { guess }')

computer_guess(1000)





























