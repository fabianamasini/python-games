import gallows_game
import guessing_game

print("*****************")
print("Choose your game!")
print("*****************")

print("[1] Gallows Game [2] Guessing Game")

game = int(input())

if game == 1:
    gallows_game.play()
elif game == 2:
    guessing_game.play()

