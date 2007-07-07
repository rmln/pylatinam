"""Nominals

This file contains classes and functions that deal with declensions
of nominals.

Nom()
Main nominal class.

Creates word methods and attributes for
given nominal.

It is possible to provide nominal as string, for example:

>>> n = Nom("puella,ae,f", nolex=True)

But, in order to force Nom() to process the noun without looking
it up, you must use nolex=True argument. You can avoid this by
calling Nomf(), which is a simple bypass with the argument:

>>> n = Nomf("puella,ae,f")

To force Nom() to try to guess/predict possible genitive form and
gender of the noun, initiate it with nominative only and without
searching the word in dictionary:

>>> n = Nomf("puella")
    
"""

__author__= "miller"
__mail__ = "cheesepy@gmail.com"
__version__="0.8.9.2"


from strings import NomStr, AdjStr, CASUS_SHORT

from latinam.ltexcept import \
    ItemNumberError, NoStemError, \
    WordListFormatError, GenderError, \
    CannotSetDeclensionError, InvalidGenitiveCompError, \
    InvalidComparationIDError
    

from latinam.lexicon.lexicon import Lex
from latinam.lexicon.lexicon import LexLookup

finder = LexLookup()

Suf = NomStr()
cas = CASUS_SHORT

class Nom:
    """Noun declension
    """
    __name__ = "Nom"
    def __init__(self, nword, pos="n", nolex=False):
        self.nolex = nolex
        if nolex==False:
            lex = Lex(nword, pos=pos) #current word
            self.entry = lex.entry #this is the word as defined in lex file
            self.translate = lex.lookup
        else:
            if type(nword) == str:
                nword = nword.split(",")
            if len(nword) != 3:
                nword = [nword[0],"",""]
            self.entry = nword
            self.lookup = None
            self.translate = finder.find(nword[0])
        self.pos=pos
        self.word = nword
        #check_n(self.entry)
        ##
        declension = dec(self.entry, pos)   #runs through the functions and returns:
        self.casii = declension[0]          #cases of the nominal
        self.type  = declension[1]          #unique id of declension
        self.suf   = declension[2]          #suffixes used
        self.stem  = declension[3]          #stem

    def show(self, detail=1):
        """Print out the cases.
        This is auxiliary function and is used for convenient
        display of results; it is also used by tools.out.py to
        create files.
        """
        n = self.entry
        t = self.translate
        print "\n", "NOUN DECLENSION", "\n", 70*"-"
        print "Noun:           ", n[0]+",", "-"+str(n[1])+",", n[2]
        if len(t) and detail==1:
            print "Translation(s): ", t
        print
        for i in range(6):
            print cas[i], self.casii[i].ljust(20, " "), cas[i+6], self.casii[i+6]
        print
        if detail > 1:
            if self.nolex:
                print "Lexicon not used."
            else:
                print "Lexicon used."
            print "Module version", __version__

    def ident(self, word):
        """identify nominal's case"""
        for case in range(12):
            if word == self.casii[case]:
                print cas[case], case

    def __getitem__(self, case):
        """get .casii value"""
        return self.casii[case]
        

class Nomf(Nom):
    """bypass Nom() class with nolex=True value"""
    def __init__(self, word):
        Nom.__init__(self, word, pos="n", nolex=True)


def dec(nominal, pos):
    """Declension."""
    allcasi = []            #store created cases here
    findd = fdec(nominal)   #find declension
    suffixes = findd[0]
    stem = stem_n(nominal, suffixes)
    i = 0
    for suffix in suffixes:
        if i == 0:
            casus = nominal[0]
        else:
            #are there any irregularities?
            check_irr = irrchg_n(stem, suffixes, i, nominal[0], nominal[1])
            if  check_irr == None:   
                casus = "%s%s" % (stem, suffix)
            else:
                casus = check_irr
        allcasi.append(casus)
        i += 1
    return allcasi, findd[1], findd[0], stem #here are the cases!


def check_n(nominal):
    """(soon defunct)
    Checks if basic requirements for declension are met.
    Returns nothing if 'what' is ok, otherwise rises error.
    Checks if:
        - has three items
        - word list is empty
        - gender is m/f/n
    """
    if len(nominal) != 3:
        raise ItemNumberError
    g = nominal[2]
    check_gender_reference = (g == "m") or (g == "f") or (g == "n")
    if (nominal[0] == "") or (nominal[1] == ""):
        raise ItemNumberError
    if check_gender_reference == False:
        raise ItemNumberError
        
    
def irrchg_n(stem, declension, case, nom, gen=None):
    """
    Grammatical irregularities of given nominal.
    This function requires the following to work:
        - stem of the nominal
        - declension strings (suffixes)
        - case of the nominal
        - nomintive of the nominal
        - genitve
    """
    # Not all nouns follow the same pattern. This
    # code regulates some "exceptions". For example,
    # nouns in 3rd dec. ending in -e have vocative
    # *and* ablative same as nominative.

    # Second:
    if declension == Suf.D2:
        #Here is one rare exception that nominative
        #is not same as vocative, and applies to
        #II declension masc. -us,-i.
        if nom.endswith("us") and gen=="i" \
        and case == 4:
            return "%s%s" % (stem, "e")
                
        
    # Third declension --------------->
    if declension == Suf.D4:
        if case == 0 or case == 4:
            if stem.endswith("c") or stem.endswith("g"):
                # Examlpes for this are nouns
                # like dux,ducis and lex,legis
                return "%s%s" % (stem[0:len(stem)-1], "x")
            else:
                return stem
    if declension == Suf.D5:
        if case == 3:
            return nom
    if declension == Suf.D6:
        if case == 3 or case == 4:
            return nom
    # Third declension end ----------->
                          

def stem_n(word, declension):
    """Stem of the noun.
    If entry is not comma delimited (ie: "puella,ae") the program
    should try to find the root based on available data.

    To state that noun change has elusive e, supply full and
    valid genitive.
    
    Ie: liber,libri  - elusive *
        liber,liberi - not elusive
        liber,i      - not elusive

    * valid form for this noun
    """
    
    nominative = word[0]
    genitive   = word[1]
    gender     = word[2]
    base       = blend(nominative, genitive, gender)
    
    if declension == Suf.D1:
        return nominative.rstrip("a") #1st dec ie. puella, -ae
    elif declension == Suf.D2:
        if nominative.endswith("us"):
            return nominative.rstrip("us") #2nd dec ie. lupus, -i
        #What follows is correction for "elusive e":
        if nominative.endswith("er"):
            if genitive.endswith("eri") or genitive=="i":
                return nominative
            else:
                return nominative.rstrip("er") + "r"
    elif declension == Suf.D3:
        return nominative.rstrip("um") #2nd dec. ie. bellum, -i (n)
    # Third declension ----------------------------->
    elif declension == Suf.D4:
        if nominative[-1] == "x":
            # from gen -is (subgroup of III dec.)
            return genitive.rstrip("is")
        else:
            return base.rstrip("is")
    elif declension == Suf.D5: return base.rstrip("is")
    elif declension == Suf.D6: return base.rstrip("is")
    elif declension == Suf.D7: return nominative.rstrip("us")
    elif declension == Suf.D8: return nominative.rstrip("u")
    elif declension == Suf.D9: return nominative.rstrip("es")
    # Third declension end-------------------------->
    else: raise NoStemError


def blend(word, gen, gd):
    """Blends nominaltive and genitive.
    Blends nominativus and genitivus (dictionary entries) to get genitive
    form. Ie: palus,udis returns paludis.
    """
    # These are different nominative and genitive
    # endings and rules for making stem to which
    # derivative endings (strings in Dx) will be added
    if word.endswith("us") and gen == "oris":
        return "%s%s" % (word[:-2], gen)
    if word.endswith("es") and gen == "itis":
        return "%s%s" % (word[:-2], gen)
    if word.endswith("en") and gen == "inis":
        return "%s%s" % (word[:-2], gen)
    if word.endswith("t") and gen == "itis":
        return "%s%s" % (word[:-2], gen)
    if word.endswith("us") and gen == "eris":
        return "%s%s" % (word[:-2], gen)
    if word.endswith("ur") and gen == "oris":
        return "%s%s" % (word[:-2], gen)
    if word.endswith("al") or word.endswith("ar") and gen == "is":
        return word
    if word.endswith("e") and gen == "is":
        return word[:-1]
    #ie: homo, -inis
    w1 = word[0:-1]
    if w1[-1] == gen[0]:
        bln = "%s%s" % (w1[0:-1], gen)
    else:
        bln = "%s%s" % (w1, gen)
    return bln

def fdec(word):
    """Identify declension.
    Identify noun's declension ID (named set of prefixes D1, D2...etc).
    Finds declension of the word. Requires tuple or list as input.

    Example:

    >>> fdec(['nomen', 'inis', 'n'])
    (('', 'is', 'i', '', '', 'e', 'a', 'um', 'ibus', 'a', 'a', 'ibus'),
    'dec003b')
    """
    # Isolated leters form word[].
    # This is needed for further checking.
    lt3 = word[0][len(word[0])-3:]
    lt2 = word[0][len(word[0])-2:]
    lt1 = word[0][len(word[0])-1:]    
    # Joined boolean queries. The aim is to
    # conclude to which declension noun
    # belongs; this is done in if block
    # bellow.
    THIRD_D_CHECK_1 = (lt2 == "or" or lt2 == "os" or lt2 == "es" \
                    or lt2 == "do" or lt2 == "us" or lt2 == "go" \
                    or lt2 == "as") or (lt1 == "s" or lt1 == "o" \
                    or lt1 == "x")
    THIRD_D_CHECK_2 = (lt3 == "men" or lt2 == "us" or lt2 == "ur" \
                      or lt1 == "t")
    THIRD_D_CHECK_4 = (lt2 == "al" or lt2 == "ar") or lt1 == "e"
    
    # Find noun's declension based on following data:
    # nominative, nominative ending, genitive ending
    # and gender.

    nominative = word[0]
    genitive   = word[1]
    gender     = word[2]

    #if len(word) > 1:
    if nominative == "":
        raise WordListFormatError
    #Correction for II with elusive "e":
    if nominative.endswith("er"):
        return Suf.D2, "dec002c"
    #Guess the declension:
    if genitive == "ae" and gender == "f": # 1st
        return Suf.D1, "dec001"
    elif genitive == "i" and gender == "m": # 2nd
        return Suf.D2, "dec002a"
    elif genitive == "i" and gender == "n": #2nd
        return Suf.D3, "dec002b"
    elif genitive[len(genitive)-2:] == "is": #3rd
        if THIRD_D_CHECK_1 == True and (gender=="m" or gender=="f"):
            return Suf.D4, "dec003a"
        if THIRD_D_CHECK_2 == True and gender=="n":
            return Suf.D5, "dec003b"
        if THIRD_D_CHECK_4 == True and gender=="n":
            return Suf.D6, "dec003c"
    elif genitive == "us": #4th
        if gender == "m":
            return Suf.D7, "dec004a"
        elif gender == "n":
            return Suf.D8, "dec004b"
        else:
            raise GenderError
    elif genitive == "ei": #5th
        return Suf.D9, "dec005"
    else:
        try:
            raise ToDo_CodeGoesHere, "try to guess form of the noun"
        except:
            raise CannotSetDeclensionError

def guess(word):
    "try to guess genitive and gender"
    pass
