#!/usr/bin/python
"""Lexicon

Lexicon
=======

This module searches lexicon and dictionary files for entries.

The search is performed in very simple manner: text search line by 
line. This is convenient for small amount of data, but quite
inefficient for larger lexicon data. For now this is not a issue.

Note: Class Lex will become depreciated in favour of LexFind.

Lexicon data and file types
---------------------------

Lexicon data is in simple plain text.

Types of files:

Definition files are located in pylatinam/lexicon/lat folder. Each
definition file has prefix latin_ followed by POS ID (part of speech
identifier). For example latin_n.txt for nouns or latin_v.txt for
verbs. POS determines format of entered words.

For nouns: tempus,oris,n
For verbs: condo,condere,3,condidi
For prepositions: iuxta,3

Translation files are stored into separate directories with prefix
latin_ plus language id (latin_en, latin_sr), also located inside
lexicon folder. Patter for naming files is the same as for definition
files and the difference is in content: each file contains one comma
delimited word which is id followed by translation words.

For example:

omnius,all

Comma delimited adjective is linked and searched in latin_adj.txt
and vice versa

finitimus,adjacent,adjoining

(first word is id, everything else are translations)


Searching and processing
------------------------

When the word is entered, program will find it in definition
file and look up translation in translation files. If word is not
found in definition file, error will occur, which does not apply
for translation since translation is irrelevant for processing.

To avoid this error the user has two options:

 - update appropriate definition file

or

 - initiate class with nolex=True switch, and
   supply needed information manually

Here are examples for second option:

>>> n = Nom("puella,ae,f", nolex=True)
>>> v = Ver("laudo,laudare,1", nolex=True)

"""

__author__= "mlinar"
__mail__ = "cheesepy [a] gmail.com"
__version__="0.6.1"
__url__ = 'http://latin.languagebits.com/'


import os
import sys
import warnings

from pylatinam.pylatexcept import *
from pylatinam.morph.strings import check_pos
from pylatinam.morph.strings import POS
from pylatinam.morph.strings import LANG

#Our working path

#(The following path causes an error if tis module
# is run from IDLE)
#lexpath = os.path.dirname(__file__)
#What follows is workaround:
import foofile
lexpath = os.path.split(foofile.__file__)[0]


#constants:
EXTENSION = ".txt"
TRANSDIR = "freelang"
WORDS = "words"
LATDIR = "lat"

#labels
# TODO Make labels reusable.

labels = {"n":"Noun", "v":"Verb"}

def strip(content):
    "strip from newline"
    for i in range(len(content)):
        content[i] = content[i].strip()
    return content

    
def lexfile(pos, word="", lng="en", what="p"):
    "returned file object of requested pos"
    if what == "p":
        return file(os.path.join(lexpath, LATDIR, "latin_%s%s" % (pos,EXTENSION)), "r")
    elif what == "t":
        # To speed up the search, all files are split into files from A to X.
        single_file = os.path.join("%s_translate" % pos,"latin_%s_%s.txt" % (pos, word[0]))
        return file(os.path.join(lexpath, WORDS, single_file), "r")
    elif what=="w":
        # To speed up the search, all files are split into files from A to X.
        single_file = os.path.join(pos,"latin_%s_%s.txt" % (pos, word[0]))
        return file(os.path.join(lexpath, WORDS, single_file), "r")

class Lex:
    """
    Find word(s) to process

    Modes:
        * simple - just the properties of the word
        * full - translation and properties
        * fcont - file content is returned

    """
    def __init__(self, word="", pos="n", mode="words", lng="en"):
        
        check_pos(pos) #check if pos is ok
        
        self.word = word
        self.pos = pos
        self.lng = lng
        self.translate = self.find_translate(word, pos).strip()

        if (mode == "simple" or mode == "full" or mode=="words") and word == "":
            raise "Provide word in Lex."

        if mode == "simple":
            self.entry = self.entry(word, pos)
        elif mode == "full":
            self.entry = self.entry(word, pos)
            self.meaning = self.translate(word, pos, lng)
        elif mode == "fcont":
            self.corpus = strip(lexfile(pos).readlines())
        elif mode == "words":
            self.entry = self.entry(word, pos, what="w")
        elif mode == "idle":
            pass
        else:
            raise LexModeError

    def __repr__(self):
        "printable thing"

        msg = """
        ----------------------
        %s
        ----------------------
        Part of speech: %s
        Class entry: %s
        Translation: %s
        """ % (",".join(self.entry), labels[self.pos], ",".join(self.entry), self.translate)

        return msg

    def entry(self, word, pos, what="p"):
        """Search lexicon file"""
        allitems = lexfile(pos, word=word, what=what).readlines()
        found = False
        match = []
        for item in allitems:
            if not item.startswith("#"):
                item = item.lower()
                lexicon_entry = item.strip().split(",")
                if lexicon_entry[0] == word: #exact match
                    if lexicon_entry not in match:
                        match.append(lexicon_entry)
        if len(match):
            return match
        else:
            raise LexiconItemNotFoundError

    def find_translate(self, word, pos, lng="en"):
        """Search translation.
        Looks up the word in corresponding dictionary.
        """
        available = ("n","v")
        if pos not in available:
             warnings.warn("Translation for POS not available.")
             return ""
        if isinstance(word, list) or isinstance(word, tuple):
            word = word[0]
        allitems = lexfile(pos, word=word, what="t", lng=lng).readlines()
        for item in allitems:
            if item.startswith(word):
                return item.split("  ::  ")[1]
        return ""
        

#Class to me used in classes that need lexicon:

class LexContainer:

    def __init__(self, nword, pos="n", nolex=False, mode="words"):
        if nolex==False:
            lex = Lex(nword, pos=pos, mode=mode)
            self.entryall = lex.entry
            # This is to keep the compatibility;
            # first item in all found is selected.
            self.entry = self.entryall[0]
            self.translate = lex.translate

            for item in range(len(self.entryall)):
                for single in range(len(self.entryall[item])):
                    self.entryall[item][single] = self.entryall[item][single].strip()
        else:
            if type(nword) == str:
                nword = nword.split(",")
            self.entry = nword
            try:
                self.translate = Lex(nword[0], pos=pos, mode=mode).translate
            except LexiconItemNotFoundError:
                self.translate = "not found"
            
                
        for i in range(len(self.entry)):
            self.entry[i] = self.entry[i].strip()
            
        self.pos=pos
        self.word = nword
        

#dummies:
class LexFind:
    pass

class LexLookup:
    pass

# tools

def lex_sort():
    "sort contents in the files aphabetically"
    for part in POS:
        print "Opening %s file..." % part
        f = open(os.path.join(lexpath, LATDIR, "latin_%s%s" % (part,EXTENSION)), "r")
        print "Reading..."
        allitems = f.readlines()
        print "Items: %s" % len(allitems)
        if len(allitems) > 0:
            print "Sorting from %s to %s..." % (allitems[0].strip(), allitems[-1].strip())
            allitems.sort()
        else:
            print "File empty. Cannot sort."
        f.close()
        f = open(os.path.join(lexpath, LATDIR, "latin_%s%s" % (part,EXTENSION)), "w")
        print "Saving."
        f.writelines(allitems)
        print "Done."
        f.close()
        print "-"*50
    
