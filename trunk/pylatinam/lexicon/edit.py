"""LEXICON

Simple console editor for lexicon files.

"""
__author__= "miller"
__mail__ = "cheesepy@gmail.com"
__version__="0.1"


from latinam.lexicon.lexicon import EXTENSION, lexpath, translatepath
from latinam.morph.strings import check_pos, POS, LANG

class LexEdit:
    "add, remove, compare, sort items in lexicone"
    def __init__(self, lng=None):
        from sys import exit as end
        self.end = end
        print "-"*58, '\nLexicone file editor\n', "-"*58
        if lng == None:
            lng = raw_input("Language? ").strip()
        if self.open_files(lng) == False:
            print "All files could not be opened. Aborting."
            self.end()
        self.lng = lng
        self.loop()

    def open_files(self, lng):
        try:
            self.f = {}
            for item in POS:
                lx = open('%s\latin_%s%s' % (lexpath,item,EXTENSION),"a")
                tr = open(('%s\\lexicon\\latin_%s\\latin_%s_%s%s')\
                          % (translatepath,lng,item,lng,EXTENSION), "a")
                self.f[item]=(lx,tr)
        except:
            return False

    def close_files(self):
        "close all opened files"
        for item in self.f.keys():
            self.f[item][0].close()
            self.f[item][1].close()

    def msg(self, prompt=None):
        "simple input"
        return raw_input(prompt).strip().lower()

    def loop(self):
        "loop and process saves until user quits"
        while -1:
            part_of_sppech = self.get_pos() 
            entry = getattr(self, "add_%s" % part_of_sppech)()
            self.save(entry, part_of_sppech)

            if self.msg("Continue (y for yes)? ") != "y":
                self.close_files()
                self.end()

    def save(self, entry, part_of_sppech):
        "save words to files"
        word = ",".join(entry[0])
        #tr = ",".join(entry[1])
        tr = entry[1]
        #
        self.f[part_of_sppech][0].write("%s\n" % word)
        self.f[part_of_sppech][0].flush()
        if tr != None:
            self.f[part_of_sppech][1].write("%s,%s\n" % (entry[0][0], tr))
            self.f[part_of_sppech][1].flush()
        print "Done for %s." % word

    def get_pos(self):
        "get POS id"
        while -1:   
            pos = self.msg("POS: ")
            if not check_pos(pos, False):
                print "Enter valid part of speech id. "
            else:
                return pos

    def add_n(self):
        "add noun to file"
        tr = None
        while -1:
            noun = self.msg("Enter noun,genitive,gender: ")
            if not noun.count(",") == 2:
                print "Invalid entry. Repeat."
                self.add_n()
            noun = noun.split(",")
            print "Search key is %s. " % noun[0]
            if self.msg("Enter translation (y for yes)? ") == "y":
                tr = self.msg("Translation for %s of word %s: "
                              % (LANG[self.lng], noun[0]))
            return noun, tr
