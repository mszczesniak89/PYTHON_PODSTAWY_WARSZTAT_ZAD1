import random

computer_choice = random.randint(1, 100)
user_guess = 0
while True:
    try:
        user_guess = int(input("Guess the number: "))
        if user_guess < computer_choice:
            print("Too small!")
        elif user_guess > computer_choice:
            print("Too big!")
        elif user_guess == computer_choice:
            print("You win!")
            break
    except ValueError:
        print("It's not a number!")
