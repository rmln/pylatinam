"""Strings (affixes etc.) and helpers

This module contains various strings, some of them organized into 
classes. The strings are used for making Latin words and various 
analysis.

TODO: VerStr should have same/similar names as in vkeys dictionary.

"""
__author__= "mlinar"
__url__ = "http://www.pylatinam.com/"
__mail__ = "cheesepy [a] gmail.com"
__version__="0.2.3.1"



import sys
import os

from pylatinam.pylatexcept import  *

# ------------------------------------------------------
s = "Non ignavia, sed industria scientiam augemus."
punctuation = '.',',',';',':','!','?'
POS = "n","v","adj","adv","prep","conj", "intj"

#Lists of words that kee 'e' in stem,
#unlike those with 'fleeting e'"""
keepe_II = ['puer','vir', 'tener','gener']

#Lists of nouns in 2nd masc. that keep
#vocative equal to nominative
noexept_2ndmsc = ['deus']

#Consonantes - the consonants
CONS =('b','c','d','f','g','h','k','l','m','n','p','q','r','s', \
       't','v','x','y','z')
#Vocales - the vocals
VOCA = ('a','e','i','o','u')
#Diphthongs
DIPH = ('au','eu','ei','ai','oi','ui')

# different helpers:

def is_vocal(letter):
    "is letter a vocal"
    if letter.lower().strip() in VOCA:
        return True
    else:
        return False

def is_cons(letter):
    "is letter a consonant"
    if letter.lower().strip() in CONS:
        return True
    else:
        return False

def is_consgroup(group, n=2):
    "check if n letters from left are consonants"
    if len(group) < n:
        #raise WordLengthInsufficientError
        return False
    group = list(group)
    group.reverse()
    for i in range(n):
        if not is_cons(group[i]):
            return False
    return True

def hyphenate(word="foederatus"):
    """Hyphenation of the word"""
    pass


# helpers end here

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

# This is obsolete and stays here for refactoring reasons.
#
### Strings for verbs -------------------------------------------------
##
##tkeys =  {'ipra':'Indicative present active', \
##         'iima':'Indicative imperfect active', \
##         'futa1':'Future active I', \
##         'iper':'Indicative perfect active', \
##         'iplu':'Indicative pluperfect active', \
##         'futa2':'Indicative future I', \
##         'imp1':'Indicative imperative I', \
##         'imp2':'Indicative imperative II or Future imperative',\
##         'ipp':'Indicative present passive',\
##         'iimperp':'Indicative imperfect passive',\
##         'futp1': 'Future passive I', \
##         'iperp': 'Indicative perfect passive',\
##         'iplperp': 'Indicative imperfect passive' }
##
##pkeys = {'parpp': 'Participle perfect passive'}

# Strings for verbs, version 2 -------------------------------------
vkeys = {'ind_a_pr':'Indicative Active Present', \
'ind_p_pr':'Indicative Passive Present', \
'sub_a_pr':'Subjunctive Active Present', \
'sub_p_pr':'Subjunctive Passive Present', \
'imp_a_pr':'Imperative Active Present', \
'imp_p_pr':'Imperative Passive Present', \
'ind_a_im':'Indicative Active Imperfect', \
'ind_p_im':'Indicative Passive Imperfect', \
'sub_a_im':'Subjunctive Active Imperfect', \
'sub_p_im':'Subjunctive Passive Imperfect', \
'ind_a_fu':'Indicative Active Future', \
'ind_p_fu':'Indicative Passive Future', \
'imp_a_fu':'Imperative Active Future', \
'imp_p_fu':'Imperative Passive Future', \
'ind_a_pe':'Indicative Active Perfect', \
'ind_p_pe':'Indicative Passive Perfect', \
'sub_a_pe':'Subjunctive Active Perfect', \
'sub_p_pe':'Subjunctive Passive Perfect', \
'ind_a_pl':'Indicative Active Pluperfect', \
'ind_p_pl':'Indicative Passive Pluperfect', \
'sub_a_pl':'Subjunctive Active Pluperfect', \
'sub_p_pl':'Subjunctive Passive Pluperfect', \
'ind_a_fp':'Indicative Active Future Perfect', \
'ind_p_fp':'Indicative Passive Future Perfect', \
'par_a_pr':'The present active participle', \
'par_p_pr':'The perfect passive participle', \
'par_a_fu':'The future active participle', \
'inf_a_pr':'The present active infinitive', \
'inf_p_pr':'The present passive infinitive', \
'inf_a_pe':'The perfect active infinitive', \
'inf_p_pe':'The perfect passive infinitive', \
'inf_a_fu':'The future active infinitive', \
'inf_p_fu':'The future passive infinitive', \
'supn':'The supine', \
'ged':'The gerund', \
'gev':'The gerundive'}


# -------------------------------------------------------------------

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
    "Strings for adjectival derivation."
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
        self.cGr = "nouns of Greek origin"
        self.Gr = ("ae", "es", "ae", "am", "e",  "e",  "ae", "arum", "is", "as", "ae", "is")
        #
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
        self.cD5a = "nouns with consonant stems, m, f, n; ie: victor, pater, mater"
        self.D5a = ("", "is", "i", "em", "", "e", "es", "um", "ibus", "es", "es", "ibus")
	#
        self.cD6 = "III, -is m,f"
        self.D6 = ("", "is", "i", "em", "", "e", "es", "ium", "ibus", "es", "es", "ibus")
        #
        self.cD6a = "III, neutrum, -e, -al, -ar"
        self.D6a = ("", "is", "i", "", "", "i", "ia", "ium", "ibus", "ia", "ia", "ibus")
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
        self.imperative_future = "","to","to","","tote","nto"
        # Indicative present passive
        self.indicative_present_passive = "or","ris","tur","mur","mini","ntur"
        # Indicative imperfect passive
        self.indicative_imperfect_passive = "bar","baris","batur","bamur","bamini","bantur"
        # Future I passive
        self.future1_passive1n2 = "bor","beris","bitur","bimur","bimini","buntur"
        self.future1_passive3n4 = "ar","eris","etur","emur","emini","entur"
        #Participle perfect passive
        self.participle_perfect_passive = "us","a","um","i","ae","a"
        # Subjanctive active present
        self.sub_a_pr = 'm','s','t','mus','tis','nt'
        # Subjanctive passive present
        self.sub_p_pr = "r", "ris", "tur", "mur", "mini", "ntur"
