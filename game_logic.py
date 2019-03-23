import random
import word_processing
import string

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
    display_word = word_processing.display_word(random_word)
    already_guessed = []
    print(enumerated_word.values(),display_word.values())
    guesses = 8
    print("Alright, let's start! You have 8 guesses to find the missing word!")

    while guesses != 0:
        guess = input("Make your guess!")
        if guess not in string.ascii_lowercase:
            print("no digits and other funny stuff, obviously...")
            guesses -= 1
            print("Guesses left: ", guesses)
        else:
            if " ".join(display_word.values()) == " ".join(enumerated_word.values()):
                print("You won!")
                break
            elif guess in already_guessed:
                print("You daft imbecile. You guessed that already!")
            elif guess in enumerated_word.values():
                already_guessed.append(guess)
                for index, char in enumerated_word.items():
                    if guess == char:
                        display_word[index] = char
            elif guess not in enumerated_word.items():
                already_guessed.append(guess)
                print("Unfortunately there was no match")
                guesses -= 1
                print("Guesses left: ",guesses)
        print(display_word.values())

if __name__ == "__main__":
    start_game()
