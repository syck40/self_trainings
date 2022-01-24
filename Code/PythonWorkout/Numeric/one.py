import random
number = random.randint(1, 100)
print(f"Number to be guess is {number}")
while True:
    guess = int(input("Enter a guess: "))
    if guess == number:
        print(f"Yout got it")
        break

    elif guess < number:
        print(f"{guess} is too low")

    else:
        print(f"{guess} is too high")
