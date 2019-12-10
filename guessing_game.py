print("*************************")
print("Welcome to guessing game!")
print("*************************")

secret_number = 42
number_of_tries = 5
game_round = 1

while game_round <= number_of_tries:
    print("Round {} of {}".format(game_round, number_of_tries))
    guess_str = input("Enter your number: ")
    guess = int(guess_str)

    right_answer = guess == secret_number
    greater_than = guess > secret_number

    if right_answer:
        print("You're right!")
        break
    elif greater_than:
        print("You missed :( Your guess is greater than the secret number!")
        game_round = game_round + 1
    else:
        print("You missed :( Your guess is less than the secret number!")
        game_round = game_round + 1

print("\n")
print("End of the game :)")
