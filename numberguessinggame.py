import random
num=random.randint(1,100)
print('This is the number guessing game.')
print('I have a secret number that is between 1 and 100.')
print('Please enter the number you have guessed: ')
guess=int(input('Enter your guess:'))
while guess!=num:
    if guess<num:
        print('too low number')
        guess=int(input('Enter again:'))
    elif guess>num:
        print('too high number. ')
        guess=int(input('Enter again:'))

print('you have guessed the corret number.\n-------CONGRATUTLATIONS!!!!!!!-----')
    