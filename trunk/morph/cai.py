#! /usr/bin/python
"""Conjunctions, interjections, adverbs

This module contains base classes for conjunctions, interjections, adverbs
and interjections.

"""

__author__= "mlinar"
__url__ = "http://www.pylatinam.com/"
__mail__ = "cheesepy [a] gmail.com"
__version__="0.0.1"

from pylatinam.lexicon.lexicon import Lex

class Conj:
    """Class for conjunctions"""
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
