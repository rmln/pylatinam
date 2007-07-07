"""Analyse sentences - pyLatinam
"""

from latinam.morph.strings import s as snt
from latinam.morph.strings import punctuation as pn
from latinam.morph.strings import Compiled as Strings
from latinam.sintax.posfinder import posfind_c, Posfind
from texts import emerald
from sntparse import Text


Strings = Strings()

text = Text(emerald["text"]).text

#----------------> The other way

def msen(sentence):
    words = normalize(sentence).split(" ")
    for word in words:
        k = posfind_c(word)
        print "%s\tv:%s\tn:%s" % (word.ljust(10), len(k["n"]), len(k["v"]))


#----------------> One way

def asnt(sentence):
    """Identify to which part of speech word belongs to."""
    words = normalize(sentence).split(" ")
    for item in words:
        item = item.strip()
        print "%s%s%s%s%s" % (item.ljust(10), '\t : ', is_pos(item, "nominal"),\
                          '\t',is_pos(item, "verb"))

def is_pos(word,pos):
    """Is word a nominal?"""
    counter = 0
    suf = getattr(Strings, pos)
    for item in suf:
        if word.endswith(item):
            counter += 1
    return counter
            
def normalize(sentence):
    """Removes interpunction characters and converts to lowcap."""
    for item in pn:
        sentence = sentence.replace(item,"")
    
    return sentence.lower()
