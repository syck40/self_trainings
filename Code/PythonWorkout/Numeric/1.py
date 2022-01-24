import random

number = random.randint(1, 100)
print(f'Numb is {number}')

while True:
    guess = int(input("Enter :"))

    if guess < number:
        print('Too low')
    elif guess > number:
        print('Too hight')
    else:
        print('You got it')
        break
    