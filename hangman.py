import pandas as pd
import random
while True:
    word_list = pd.read_csv('wordbank.csv', header=None)
    word_list = word_list[0].tolist()
    starting_word = random.choice(word_list)
    quiz_word = list(starting_word)
    list_word = ["_" for _ in range(len(quiz_word))]
    display_word = "".join(list_word)