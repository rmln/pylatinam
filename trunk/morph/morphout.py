#! /usr/bin/python
"""
print.py
========

Code for displaying output in the console mode.

TODO

* What is with plural form of participles?

"""

__author__= "mlinar"
__url__ = "http://www.pylatinam.com/"
__mail__ = "cheesepy [a] gmail.com"
__version__ = "0.1"


#from noun import Nom
#from adjective import Adj
from strings import vkeys



class captions:
    def __init__(self):
        """text for various display messages"""
        self.Nom = {"title":"NOUN DECLENSION", "pos": "Noun: "}
        self.Ver = {"title":"CONJUGATION", "pos": "Verb: "}
        self.Adj = {"title":"ADJECTIVE DECLENSION", "pos": "Adjective: "}


class Show:

    def __init__(self, pos, detail=1, vkeys=vkeys):
        """
        Prints out relevant details.
        Here pos is a class (Nom(), Ver() etc.)
        """
        cap = getattr(captions(), pos.__name__)
        self.pos = pos
        self.vkeys = vkeys
        # head line; 
        print "\n", cap["title"], "\n", 70*"-"
        # pos specific text;
        print cap["pos"], self.text_format(pos)
        # available translations;
        if len(pos.translate) and detail==1:
            print "Translation(s): ", pos.translate
        print
        # print out the table(s);
        getattr(self, "part_%s" % pos.__name__)()
        # ending report with info about class
        # versions;
        if detail > 1:
            if pos.nolex:
                print "Lexicon not used."
            else:
                print "Lexicon used."
            #print "Module version", pos.__version__

    def text_format(self, pos):
        """Return  nicely formated pos entry"""
        if pos.entry != str:
            return " ".join(["".join((f,",")) for f in pos.entry]).strip(",")
        else:
            return pos.entry

    def part_Nom(self):   
        "print nouns"
        for i in range(6):
            print self.pos[i].ljust(20, " "), self.pos[i+6]


    def part_Adj(self):
        "print adjectives"
        pass

    def part_Ver(self):
        "print verbs"
        for tense in self.vkeys.keys():
            print self.vkeys[tense]
            print "-"*40
            #actual tense:
            try:
                ten = self.pos.tenses[tense]
                if len(ten) == 2:
                    esse = ten[1] #auxiliary verb
                    ten = ten[0] #main verb
                    for i in range(3):
                        print "%s %s".ljust(10, " ") % (ten[0], esse[i]), "%s %s" % (ten[0], esse[i+3])  
                else:
                    for i in range(3):
                        print str(ten[i]).ljust(20," "), ten[i+3]
                print
                print
            except:
                pass
        

#nom = Nom("puella")
#Show(nom)

#Show(Ver("amo"))

