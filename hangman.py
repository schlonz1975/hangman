import random

words = ["hello", "boat", "character", "justice", "marina", "football"]

# shuffle the list "words" and
# store the item at index[0] in a new list "secret_word"
random.shuffle(words)
secret_word = list(words[0])
guesses = 0
# char_guessed = False
player_guess = None
display = secret_word.copy()

# "display" gets turned into dashes for initial print
for item in range(len(display)):
    display[item] = "_"

# print(display)

# main game loop
while guesses < 11:
    # code executed per guess
    for letter in range(len(secret_word)):
        if secret_word[letter] == player_guess:
            display[letter] = secret_word[letter]

        for item in display:
            print(str(item), end=" ")

        print()
        player_guess = str.lower(input("Make a guess: "))
        guesses += 1






# loop for each guess









# for guess in range(max_guesses):
#     # check each letter if guessed and print accordingly
#     for letter in range(len(secret_word)):
#         if secret_word[letter] == player_guess:
#             print(player_guess, end=" ")
#         else:
#             print("_", end=" ")
#
#     player_guess = str.lower(input("Make a guess: "))


