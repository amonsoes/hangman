import nltk
from nltk.corpus import gutenberg


def check_pos(lst):
    nouns = [word for word,pos in nltk.pos_tag(lst) if pos.startswith("N")]
    final = []
    for word,tag in nltk.pos_tag(nouns):
        if tag != "NNP" and tag != "NNPS":
            final.append(word)
    return final


def get_words():
    bag = []
    for text in gutenberg.fileids():
        if len(bag) > 10000:
            break
        for word in gutenberg.words(text):
            if len(word) > 8:
                bag.append(word)
    return check_pos(bag)


def enum_word(word):
    return {num: char for num, char in enumerate(word.lower())}

def display_word(word):
    return {num: "_" for num, i in enumerate(enum_word(word).keys())}
