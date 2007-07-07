"""POS Finder - Latinam
Try to define part of speech for given word using lexicone.
"""

from latinam.morph.strings import POS, Compiled
from latinam.lexicon.lexicon import LexFind

nf = Compiled().nominal
vf = Compiled().verb

##nfe = Compiled().nominale
##vfe = Compiled().verbe

nfe = Compiled().n
vfe = Compiled().v

all = (nf, "n"), (vf, "v"), (nf, "adj")
alle = (nfe, "n"), (vfe, "v"), (nfe, "adj")


class Posfind:
    """POS finder via lexicon"""
    def __init__(self, word):
        self.pos = {}
        for s in all:
            self.pos[s[1]] = posfind_raw(word, s[0], s[1])
        self.entry = word
            

def posfind_raw(word, suf, posid):
    """Uses rawsearch() in lexicon.py to find part of speech"""
    result_raw = []
    for sufs in suf:
        if word.endswith(sufs):
            call = rawfind(word.rstrip(sufs), posid)
            if call != [] and result_raw.__contains__(call[0])==False:
                result_raw.extend(call)
    return result_raw

def posfind_c(word):
    """Identify word using exclusive POS strings"""
    result_compiled = {"n":[],"v":[],"adj":[]}
    for item in alle: #item ie (nfe, "n")
        for suf in item[0]: #--> nfe
            if word.endswith(suf):
                result_compiled[item[1]].append(suf)
    return result_compiled

