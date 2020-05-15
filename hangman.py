import random

words = ["hello", "boat", "character", "justice", "marina", "football"]

# shuffle the list "words" and
# store the item at index[0] in a new list "secret_word"
random.shuffle(words)
secret_word = list(words[0])
max_guesses = 11
# write empty lines for the word's characters
for item in range(len(secret_word)):
    print("_", end=" ")

# main game loop
for guess in range(max_guesses):
    print()
    player_guess = str.lower(input("Make a guess: "))
    if player_guess in secret_word:
        print("Great")





