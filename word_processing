import nltk
from nltk.corpus import gutenberg


class TextProcessing:

    def __init__(self):
        pass


    @staticmethod
    def check_pos(lst):
        return [word for word,pos in nltk.pos_tag(lst) if pos.startswith("N")]


    @staticmethod
    def get_words():
        bag = []
        for text in gutenberg.fileids():
            if len(bag) > 10000:
                break
            for word in gutenberg.words(text):
                if len(word) > 7:
                    bag.append(word)
        return check_pos(bag)

    @staticmethod
    def enum_word(word):
        return {num: char for num, char in enumerate(word)}
