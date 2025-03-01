import pandas as pd
import random
hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


while True:
    word_list = pd.read_csv('wordbank.csv', header=None)
    word_list = word_list[0].tolist()
    starting_word = random.choice(word_list)
    quiz_word = list(starting_word)
    list_word = ["_" for _ in range(len(quiz_word))]
    display_word = "".join(list_word)

    print("Welcome to hangman!")

    lives = 6
    guessed_letters = []
    while True:
        print(f"Your word: {display_word}")
        guess = input("Guess a letter: ")
        while guess in guessed_letters or not guess.isalpha():
            print("Letter already chosen / Invalid input. Please try again.")
            guess = input("Guess a letter: ")
        guessed_letters.append(guess)
        if guess in quiz_word:
            print("You got it!")
            list_word[quiz_word.index(guess)] = guess
        else:
            print("Nuh-uh!")
            lives -= 1
            if lives == 0:
                print("You lost!")
                break
        display_word = "".join(list_word)
        if display_word == starting_word:
            print("You won!")
            break
    affirm = input("Do you want to play again? (y/n)")
    if affirm == "y":
        pass
    elif affirm == "n":
        print("Thanks for playing!")
    else:
        print("Invalid input. Please try again.")
        affirm = input("Do you want to play again? (y/n)")