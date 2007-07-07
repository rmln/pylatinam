"""Conjuctions, interjections, adverbs

This module contains base classes for conjuctions, interjections, adverbs
and interjections.

"""

__author__= "miller"
__mail__ = "cheesepy@gmail.com"
__version__="0.1"

from latinam.lexicon.lexicon import Lex

class Conj:
    """Class for conjuctions"""
    __name__ = "Conj"
    def __init__(self, word):
        self.pos = "conj"
        self.entry = word
        self.translate = Lex(word, pos="conj").lookup

class Intj:
    """Class for interjections"""
    __name__ = "Intj"
    def __init__(self, word):
        self.pos = "intj"
        self.entry = word
        self.translate = Lex(word, pos="intj").lookup

class Adv:
    """Class for adverbs"""
    __name__ = "Adv"
    def __init__(self, word):
        self.pos = "adv"
        self.entry = word
        self.translate = Lex(word, pos="adv").lookup
