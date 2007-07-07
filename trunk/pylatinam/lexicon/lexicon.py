"""LEXICON
This module searches lexicon and dictionary files for entries.

The search is preformed in very simple manner: text search line by 
line. This is convenient for small amount of data, but inefficient for 
extensive data.

Class Lex will become depreciated in favour of LexFind.

"""
__author__= "miller"
__mail__ = "cheesepy@gmail.com"
__version__="0.4.4.1"


import os, sys
import pylatinamdir

lexpath = os.path.dirname(pylatinamdir.__file__)
translatepath = lexpath.strip('\lexicon')

from latinam.ltexcept import *
from latinam.morph.strings import check_pos, POS, LANG

EXTENSION = ".txt"

class LexLookup:
    def __init__(self, lng="en"):
        "inititate class"
        #try:
        tr = open(os.path.join(lexpath, "freelang", "%s.txt") % lng, "r")
        #except:
            #raise DictionaryFileOpenError, "Failed to open lexicon file."
        self.allitems = tr.readlines()
        tr.close()  

        
    def find(self, word):
        """Search translation.
        Looks up the word in corresponding dictionary.
        """
        items_found = []
        for lw in self.allitems:
            item = lw.split(" ")
            item = item[0]
            if item==word:
                lw = lw.replace("--", " - ")
                items_found.append(lw.strip())
        return "; ".join(items_found)

finder = LexLookup("en")

class Lex:
    """Find word to process (and translation, if available)"""
    def __init__(self, word, lng="en", pos="n"):
        check_pos(pos) #check if pos is ok
        self.word = word
        self.entry = self.entry(word, pos)
        self.lookup = finder.find(word)

        
    def entry(self, word, part):
        """Search lexicon file"""
        f = open(os.path.join(lexpath, "latin_%s%s" % (part,EXTENSION)), "r")
        allitems = f.readlines() #loop through lexicon data
        f.close()
        found = False
        for item in allitems:
            if not item.startswith("#"):
                lexione_entry = item.strip().split(",")
                if lexione_entry[0] == word: #exact match
                    allitems = None
                    found = True
                    break
        if found:
            return lexione_entry
        else:
            raise LexiconItemNotFoundError                
            


class LexFind:
    "search lexicons"
    def __init__(self):
        "initiate files"
        self.open_files()
        self.load_files()
        self.close_files()

    def open_files(self):
        "open files for reading"
        self.f = {}
        try:
            for item in POS:
                lx = open(os.path.join(lexpath, "latin_%s%s" % (item,EXTENSION)), "r")
                self.f[item]=lx
        except: pass

    def load_files(self):
        "load words from files"
        self.corpus = {}
        try:
            for item in POS:
                self.corpus[item]=[w.strip() for w in self.f[item].readlines()]
        except: pass

    def close_files(self):
        "close files"
        try:
            for item in self.f.values():
                item.close()
        except: pass

    def crude(self, word, pos="n", wl=None):
        "the simplest search"
        if type(wl) != "int" and wl != None:
            raise ValueError, "Word length must be integer."
        found = []
        for item in self.corpus[pos]:
            if wl==None:
                if item.startswith(word):
                    found.append(item)
            else:
                if item[:wl]==word[:wl]:
                    found.append(item)
        return found

    def crudex(self, word, pos="n", wl=None):
        "extended function crude() for all pos items"""
        found = {}
        for pos in POS:
            cf = self.crude(word, pos, wl)
            if len(cf) != 0:
                found[pos]=cf
        return found
        
