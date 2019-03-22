# hangman

this is a game, where the user (user-input) tries to guess a randomly (random module) initialized word with a character range of 7 -10 (nltk). The user can guess 8 times, until the hangman gets hanged and the player loses (else-if). The characters he guesses right will be displayed on the word (like so: _ _ _ r _ _ ), if he guesses wrong, the characters will be also diplayed, but on the side of the screen (pygame). If the user tries to take a words which he has wrongly guessed before, the algy should prevent him from doing so. (else-if)

logical script:

1. user input handling
2. random module for randomly choosing word
3. nltk for processing both the word to guess and the user input
4. wrap a complex if-else-construct

graphical script:

1. pygame
2. make screen
4. event handling
3. display everything correctly
5. display update
