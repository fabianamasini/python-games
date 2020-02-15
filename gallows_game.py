def play():
    print("************************")
    print("Welcome to gallows game!")
    print("************************")

    secret_word = "banana"
    right_answer = False
    hanged = False

    while not right_answer and not hanged:
        print("Which letter?")
        guess = input().upper().strip()
        formatted_secret_word = secret_word.upper().strip()
        index = 0

        for letter in formatted_secret_word:
            if guess == letter:
                print(f"Found letter {guess} in position {index}")
            index = index + 1


if __name__ == "__main__":
    play()
