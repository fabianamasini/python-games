import random as rdm


def play():
    print("*************************")
    print("Welcome to guessing game!")
    print("*************************")

    secret_number = round(rdm.randrange(1, 101))
    number_of_tries = 0
    points = 1000

    print("What's the difficulty level?")
    print("[1] Easy [2] Medium [3] Hard")

    level = int(input())

    if level == 1:
        number_of_tries = 20
        print(f"You have {number_of_tries} tries. Good luck!")
    elif level == 2:
        number_of_tries = 10
        print(f"You have {number_of_tries} tries. Good luck!")
    elif level == 3:
        number_of_tries = 5
        print(f"You have {number_of_tries} tries. Good luck!")
    else:
        print("Invalid level number.")

    for game_round in range(1, number_of_tries + 1):
        print(f"Round {game_round} of {number_of_tries}")
        guess_str = input("Enter your number. It must be between 1 and 100: ")
        guess = int(guess_str)

        if guess > 100 or guess < 1:
            print("Your number should be between 1 and 100. Try again.")
            continue

        right_answer = guess == secret_number
        greater_than = guess > secret_number

        if right_answer:
            print("You're right!")
            break
        elif greater_than:
            print("You missed :( Your guess is greater than the secret number!")
            lost_points = guess - secret_number
            points = points - lost_points
            continue
        else:
            print("You missed :( Your guess is less than the secret number!")
            lost_points = secret_number - guess
            points = points - lost_points
            continue

    print("\n")
    print("End of the game :)")
    print(f"The secret number was {secret_number}")
    print(f"Your final punctuation: {points}")
