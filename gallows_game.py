def play():
    print("************************")
    print("Welcome to gallows game!")
    print("************************")
    print("Here's your secret word:")

    secret_word = "banana"
    right_letters = []
    right_answer = False
    hanged = False

    def right_letters_list():
        for _ in secret_word:
            right_letters.append("_")
        return right_letters

    right_letters = right_letters_list()
    print(right_letters)

    while not right_answer and not hanged:
        print("Which letter?")
        guess = input().upper().strip()
        formatted_secret_word = secret_word.upper().strip()
        index = 0

        for letter in formatted_secret_word:
            if guess == letter:
                right_letters[index] = guess
                # print(f"Found letter {guess} in position {index}")
            index = index + 1
        print(right_letters)


if __name__ == "__main__":
    play()
