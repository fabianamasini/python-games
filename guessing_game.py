print("*************************")
print("Welcome to guessing game!")
print("*************************")

secret_number = 42
guess_str = input("Enter your number: ")
guess = int(guess_str)

if guess == secret_number:
    print("You're right!")
else:
    print("You missed :(")
print("End of the game :)")
