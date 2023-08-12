#!/usr/bin/python3
'''This is a quiz game that prompt a user to enter a number
    within a range of numbers
'''

import random
attempt = 1
number = 0
name = str(input('please enter your name: '))
random = random.randint(1, 10)


print(f'Hello {name}, a number has been selected between 1 - 10')
while(number < 10):
    number = int(input('Guess the number: '))
    if number ==  random:
        print(random)
        attempt += 1
        if attempt > 10:
            print(f'{name} You have exceeded your limit')
            print('You lose')
            break;
        if number < 10 and random > 10:
            print("number is greater than 10")
       """ elif number < 20 and random > 20:
            print("number is greater than 20")
        elif number < 30 and random > 30:
            print("number is greater than 30")
        elif number < 40 and random > 40:
            print("number is greater than 40")
        elif number < 50 and random > 50:
            print("number is greater than 50")
        elif number < 60 and random > 60:
            print("number is greater than 60")
        elif number < 70 and random > 70:
            print("number is greater than 70")
        elif number < 80 and random > 80:
            print("number is greater than 80")
        elif number < 90 and random > 90:
            print("number is greater than 90")
        elif random <100:
            print(f"number is greater than 100")
        """
        else:
            print(random)
print(random)
