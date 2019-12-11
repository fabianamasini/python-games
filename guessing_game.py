import random as rdm

print("*************************")
print("Welcome to guessing game!")
print("*************************")

secret_number = round(rdm.randrange(1, 101))
number_of_tries = 5
game_round = 1

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
        continue
    else:
        print("You missed :( Your guess is less than the secret number!")
        continue

print("\n")
print("End of the game :)")
print(f"The secret number was {secret_number}")
