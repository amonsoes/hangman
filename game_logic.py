import random
import word_processing

words = word_processing.get_words()


def start_game():
    print("Welcome to Hangman!")
    choice_1 = input("Would you like to play? y/n")
    if choice_1 == "y":
        game()
    else:
        print("Alrighty then, ye butthole.")


def game():
    random_word = words[random.randint(0, len(words))]
    enumerated_word = word_processing.enum_word(random_word)
    guesses = 8
    print("Alright, let's start! You have 8 guesses to find the missing word!")
    
    while guesses != 0:
        guess = input("What character do you want to pick?")
        if guess in enumerated_word.values()

