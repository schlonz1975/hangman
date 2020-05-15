import random

words = ["hello", "boat", "character", "justice", "marina", "football"]

# shuffle the list "words" and
# store the item at index[0] in a new list "secret_word"
random.shuffle(words)
secret_word = list(words[0])
max_guesses = 11
char_guessed = False
player_guess = None
# loop for each guess
for guess in range(max_guesses):
    # check each letter if guessed and print accordingly
    for letter in range(len(secret_word)):
        if secret_word[letter] == player_guess:
            print(player_guess, end=" ")
        else:
            print("_", end=" ")

    player_guess = str.lower(input("Make a guess: "))


