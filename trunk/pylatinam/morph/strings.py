"""String module - pyLatinam package

This module contains various strings, some of them organized into 
classes. The strings are user for making Latin words and various 
analysis.

"""
__author__= "miller"
__mail__ = "cheesepy@gmail.com"
__version__="0.4.2"


import sys, os

from latinam.ltexcept import  UndefinedPOSError

s = "Non ignavia, sed industria scientiam augemus."

punctuation = '.',',',';',':','!','?'
POS = "n","v","adj","adv","prep","conj", "intj"

CASES = "nominativus sng", "genitivus sng", "dativus sng",  \
	"accusativus sng", "vocativus sng", "ablativus sng",  \
	"nominativus pl", "genitivus pl", "dativus pl",  \
	"accusativus pl", "vocativus pl", "ablativus pl"

CASUS_SHORT = "Nom. s.", "Gen. s.", "Dat. s.", \
              "Acc. s.", "Voc. s.", "Abl. s.", \
              "Nom. p.", "Gen. p.", "Dat. p.", \
              "Acc. p.", "Voc. p.", "Abl. p." 

CASUS_CLASS = "noms", "gens", "dats", "accs", \
              "vocs", "abls", "nomp", "genp", \
              "datp", "accp", "vocp", "ablp"

LANG = {'en':"English", 'sr':"Serbian", 'lt':"Latin"}

def check_pos(what, stop=True):
    """Checks is right "part of speech" (pos) string
    is valid.
    """
    if POS.__contains__(what):
        return True
    else:
        if stop==True:
            raise UndefinedPOSError, \
            "Part of speech (POS) you provided is not defined."
        else:
            return False

class AdjStr:
    __name__ = "AdjStr"
    def __init__(self):
        self.nomgen = ('us','i', 'm'),('er','i', 'm'),\
                      ('a','ae', 'f'), ('um','i', 'n')
        self.akeys = 'm1','m2','f','n'

class NomStr:
    """
    Strings for nominal derivation (NomStr class)
    """
    __name__ = "NomStr"
    def __init__(self):
        #declensions------->
        self.cD1 = "nouns and adjectives, female, ending in -a"
        self.D1 = ("a", "ae", "ae", "am", "a",  "a",  "ae", "arum", "is", "as", "ae", "is")
        #
        self.cD2 = "nouns and adjectives,,ending in -o"
        self.D2 = ("us", "i", "o", "um", "e",  "o",  "i", "orum", "is", "os", "i", "is")
        #
        self.cD3 = "nouns and adjectives, neutrum, ending in -o"
        self.D3 = ("um", "i", "o", "um", "um",  "o",  "a", "orum", "is", "a", "a", "is")
        #
        self.cD4 = "nouns with consonant stem, masculinum & femininum, -oris, -inis, -itis"
        self.D4 = ("s", "is", "i", "em", "s", "e",  "es",  "um", "ibus", "es", "es", "ibus")
        #
        self.cD5 = "nouns with consonant stem, neutrum, -oris, -minis, -eris"
        self.D5 = ("", "is", "i", "", "", "e", "a", "um", "ibus", "a", "a", "ibus")
        #
        self.cD6 = "III, neutrum, -e, -al, -ar"
        self.D6 = ("", "is", "i", "", "", "i", "ia", "ium", "ibus", "ia", "ia", "ibus")
        #
        self.cD7 = "nouns, masculinum, -us (IV declension)"
        self.D7 = ("us", "us", "ui", "um", "us", "u", "us", "uum", "ibus", "us", "us", "ibus")
        #
        self.cD8 = "nouns, neutrum, -us (IV declencion)"
        self.D8 = ("u", "us", "u", "u", "u", "u", "ua", "uum", "ibus", "ua", "ua", "ibus")
        #
        self.cD9 = "nouns, -es,ei (V declension)"
        self.D9 = ("es", "ei", "ei", "em", "es", "e", "es", "erum", "ebus", "es", "es", "ebus")
        #
        self.adj = 'or','oris','ori','orem','or','ore','ores','orum','oribus','ores','ores','ibus'
        #
        self.cDALL = "All declension strings combined together"
        self.DALL = self.D1, self.D2, self.D3, self.D4, self.D5, \
                    self.D6, self.D7, self.D8, self.D9

class VerStr:
    """
    Strings that are used for making verb inflexions.
    """
    __name__ = "VerStr"
    def __init__(self):
        self.infinitive_endings = "are", "ere", "ire"
        self.perfect = "avi", "evi", "ivi"
        # are - indicative present active - 1
        #self.indicative_present = "indicative present active (are)"
        self.indicative_present = "o", "s", "t", "mus", "tis", "nt"
        # ere - mixed conjugations (cupio, statuo)
        self.mpr1 = "o", "s", "t", "mus", "tis", "unt"
        self.mpr2 = "o", "is", "it", "imus", "itis", "unt"
        self.mimp = "ebam", "ebas", "ebat", "ebamus", "ebatis", "ebant"
        # Future I
        self.future1n2= "bo","bis","bit","bimus","bitis","bunt"
        self.future3n4= "am","es","et","emus","etis","ent"
        # Perferct
        self.perfect = "i", "isti", "it", "imus", "istis", "erunt"
        # Pluperfect active ind.
        self.ind_act_pluperfect = "eram", "eras", "erat", "eramus", "eratis", "erant"
        # Future II indicative
        self.future2 = "ero", "eris", "erit", "erimus", "eritis", "erint"
        # Imperative II (Imperative future)
        self.imperative_future = None,"to","to",None,"tote","nto"
        # Indicative present passive
        self.indicative_present_passive = "or","ris","tur","mur","mini","ntur"
        # Indicative imperfect passive
        self.indicative_imperfect_passive = "bar","baris","batur","bamur","bamini","bantur"
        # Future I passive
        self.future1_passive1n2 = "bor","beris","bitur","bimur","bimini","buntur"
        self.future1_passive3n4 = "ar","eris","etur","emur","emini","entur"
        #Participle perfect passive
        self.participle_perfect_passive = "us","a","um","i","ae","a"
        

# Statistic code and other things, not
# primaraly user for inflexion, follow:

class Compiled:
    __name__ = "Compiled"
    def __init__(self):
        
        self.verb=('','bor', 'beris', 'bitur', 'bimur', 'bimini', 'buntur', 'ar',
        'eris', 'etur', 'emur', 'emini', 'entur', 'bo', 'bis', 'bit',
        'bimus', 'bitis', 'bunt', 'ero', 'erit', 'erimus', 'eritis',
        'erint', 'am', 'es', 'et', 'emus', 'etis', 'ent', 'to', 'tote',
        'nto', 'eram', 'eras', 'erat', 'eramus', 'eratis', 'erant', 'bar',
        'baris', 'batur', 'bamur', 'bamini', 'bantur', 'o', 's', 't', 'mus',
        'tis', 'nt', 'or', 'ris', 'tur', 'mur', 'mini', 'ntur', 'are', 'ere',
        'ire', 'ebam', 'ebas', 'ebat', 'ebamus', 'ebatis', 'ebant', 'unt',
        'is', 'it', 'imus', 'itis', 'us', 'a', 'um', 'i', 'ae', 'isti', 'istis',
        'erunt', 'vi')
        
        self.nominal=('','a', 'ae', 'am', 'arum', 'is', 'as', 'us', 'i', 'o', 'um',
        'e', 'orum', 'os', 's', 'em', 'es', 'ibus', 'ia', 'ium', 'ui',
        'u', 'uum', 'ua', 'ei', 'erum', 'ebus')

        self.nominale = ('arum', 'as', 'e', 'orum', 'os', 'em', 'ibus', 'ia', 'ium',
                         'ui', 'u', 'uum', 'ua', 'ei', 'erum', 'ebus')
        self.verbe = ('bor', 'beris', 'bitur', 'bimur', 'bimini', 'buntur', 'ar',
                      'eris', 'etur', 'emur', 'emini', 'entur', 'bo', 'bis', 'bit',
                      'bimus', 'bitis', 'bunt', 'ero', 'erit', 'erimus', 'eritis',
                      'erint', 'et', 'emus', 'etis', 'ent', 'to', 'tote', 'nto',
                      'eram', 'eras', 'erat', 'eramus', 'eratis', 'erant', 'bar',
                      'baris', 'batur', 'bamur', 'bamini', 'bantur', 't', 'mus',
                      'tis', 'nt', 'or', 'ris', 'tur', 'mur', 'mini', 'ntur',
                      'are', 'ere', 'ire', 'ebam', 'ebas', 'ebat', 'ebamus',
                      'ebatis', 'ebant', 'unt', 'it', 'imus', 'itis', 'isti',
                      'istis', 'erunt', 'vi')

        self.n = ('arum', 'as', 'orum', 'os', 'em', 'ibus', 'ia', 'ium',
                  'ui', 'u', 'uum', 'ua', 'ei', 'erum', 'ebus')

        self.v = ('bor', 'beris', 'bitur', 'bimur', 'bimini', 'buntur',
                  'ar', 'eris', 'etur', 'emur', 'emini', 'entur', 'bo',
                  'bis', 'bit', 'bimus', 'bitis', 'bunt', 'ero', 'erit',
                  'erimus', 'eritis', 'erint', 'et', 'emus', 'etis',
                  'ent', 'to', 'nto', 'eram', 'erat', 'eramus', 'eratis',
                  'erant', 'bar', 'baris', 'batur', 'bamur', 'bamini',
                  'bantur', 't', 'mus', 'tis', 'nt', 'or', 'ris', 'tur',
                  'mur', 'mini', 'ntur', 'ere', 'ebam', 'ebat', 'ebamus',
                  'ebatis', 'ebant', 'unt', 'it', 'imus', 'itis', 'isti',
                  'istis', 'erunt', 'vi')
