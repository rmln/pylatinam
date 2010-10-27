#! /usr/bin/python
"""Nominals (primarily nouns)

Nominals
========

This file contains classes and functions for declensions
of nominals, primarily nouns.

Nom() - Main nominal class
--------------------------

This class creates word-methods and attributes for given nominal. In practice
this means that this module will:

 - Create six cases of Latin nominal. The order of the cases is: nominative, 
 genitive, dative, accusative, vocative and ablative).

In order to do the above, module must process nominative, genitive and gender
of the noun. Some of the processing includes, but is not limited to:

 - Finding stem of the noun - stem_n()
 - Checking against irregularities - irrchg_n()
 - Creating proper form with 'fleeting e' words - fleetinge()
 - Making full form by combining nom. and shortened gen. - blend()
 - Checking if gen. is full or shortened - is_fullgen()
 - Deciding declension and returning suffixes - fdec()

These functions are reusable as separate objects and that is why I did not wrap
them in the separate class: Nom() class is just a string container for 
functions' outputs.


The class should receive Latin word as tuple or list. However, it is possible to
provide nominal as string, for example:

>>> n = Nom("puella,ae,f", nolex=True)

In order to force Nom() to process the noun without looking it up,nolex=True 
argument should be used. Shorten the call by Nomf(), which is a simple bypass
with the argument already provided:

>>> n = Nomf("puella,ae,f")

TODO: predict genitive
TODO: blending gen & nom when genitive is more than suffix.
    
"""


__author__= "mlinar"
__url__ = "http://latin.languagebits.com/"
__mail__ = "cheesepy [a] gmail.com"
__version__="0.2.3.5.2"


from strings import NomStr, AdjStr, CASUS_SHORT
from strings import is_consgroup, is_cons, keepe_II, noexept_2ndmsc

from pylatinam.pylatexcept import \
    ItemNumberError, NoStemError, \
    WordListFormatError, GenderError, \
    CannotSetDeclensionError, InvalidGenitiveCompError, \
    InvalidComparationIDError, BlendingError
    

from pylatinam.lexicon.lexicon import LexContainer
from morphout import Show
import irreg 

# Until the code that makes base for
# some words is improved, let us treat
# problematic nouns as exceptions:
hack_nouns = {"mos":"mor"}

Suf = NomStr()
cas = CASUS_SHORT

class Nom:
    """Noun declension
    """
    
    __name__ = "Nom"

    __congru__ = "Adj", "Ver"
    
    def __init__(self, nword, pos="n", nolex=False, mode="words"):
        "init"
        container = LexContainer(nword, pos=pos, nolex=nolex, mode=mode)
        self.entry = container.entry
        self.word = container.word
        self.pos = container.pos
        self.translate = container.translate
        self.nolex = nolex
        ##
        exception = self.is_exception(self.entry)
        if not exception:
            declension = dec(self.entry, pos)   #runs through the functions and returns:
            self.casii = declension[0]          #cases of the nominal
            self.type  = declension[1]          #unique id of declension
            self.suf   = declension[2]          #suffixes used
            self.stem  = declension[3]          #stem
        else:
            self.casii = exception[0]
            self.type  = exception[1]
            self.suf   = exception[2]
            self.stem  = exception[3]
            

    def is_exception(self, entry):
        "check if a noun is an exception"
        entry = ','.join(entry)
        if entry in irreg.irreg_nom.keys():
            return irreg.irreg_nom[entry]
        else:
            return False

    def show(self, detail=None):
        """Print out the cases.
        """
        Show(self)

    def ident(self, word):
        """Identify nominal's case"""
        case_match = []
        for case in range(12):
            if word == self.casii[case]:
                case_match.append(case)
        return case_match

    def __getitem__(self, case):
        """Get .casii value"""
        return self.casii[case]
        

class Nomf(Nom):
    """Bypass Nom() class with nolex=True value"""
    def __init__(self, word):
        Nom.__init__(self, word, pos="n", nolex=True)


def dec(nominal, pos):
    """Declension"""
    allcasi = []            #store created cases here
    find_declension = fdec(nominal)   #find declension
    suffixes = find_declension[0]
    stem = stem_n(nominal, suffixes)
    i = 0
    for suffix in suffixes:
        if i == 0:
            casus = nominal[0]
        else:
            #are there any irregularities?
            n = nominal[0]
            g = nominal[1]
            gender = nominal[2]
            check_irr = irrchg_n(stem=stem, declension=suffixes, \
                                 case=i, nom=n, genitive=g, gen=gender)
            if  check_irr == None:
                casus = "%s%s" % (stem, suffix)
            else:
                casus = check_irr
        allcasi.append(casus)
        i += 1
    return allcasi, find_declension[1], find_declension[0], stem #here are the cases!


def check_n(nominal):
    """Soon defunct!
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
        
    
def irrchg_n(stem, declension, case, nom, genitive, gen=None):
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

    #First
    if declension == Suf.Gr:
        if case == 2:
            return blend(nom, genitive, gen)

    # Second:
    if declension == Suf.D2:
        #Here is one rare exception when nominative
        #is not the same as vocative, and applies to
        #II declension masc. -us,-i.
        #List of exceptions is in noexept_2ndmsc.
        if nom in noexept_2ndmsc and case == 4:
            return nom
        if nom.endswith("us") and genitive=="i" and case == 4:
            return "%s%s" % (stem, "e")

        #Nouns that have zero ending in vocative
        # ie. puer,-i; liber,-i
        if (nom.endswith("er") or nom.endswith("r")) and (genitive.endswith("i") and case == 4):
            return nom
                
        
    # Third declension --------------->
    if declension == Suf.D4:
        if case == 0 or case == 4:
            if stem.endswith("c") or stem.endswith("g"):
                # Examlpes for this are nouns
                # like dux,ducis and lex,legis
                return "%s%s" % (stem[0:len(stem)-1], "x")
            else:
                return nom
            
    if declension == Suf.D5a and nom.endswith('er'):
        # This is for "fleeting e". For noun 'pater'
        # vocative in the program is part instead
        # of 'pater'
        if case == 4:
            return nom
    if declension == Suf.D5 and gen=='n':
        if case == 4 or case == 3:
            return nom
    if declension == Suf.D6:
        if case == 4:
            return nom
    if declension == Suf.D6a:
        if case == 3 or case == 4:
            return nom
    # Third declension end ----------->
                          

def stem_n(word, declension):
    """
    Stem of the noun.
    If entry is not comma delimited (ie: "puella,ae") the program
    should try to find the root based on available data.

    To state that noun change has fleeting e, supply full and
    valid genitive.
    
    Ie::
    
    liber,libri  - fleeting *
        liber,liberi - not elusive
        liber,i      - not elusive

    * valid form for this noun
    """
    
    nominative = word[0]
    genitive = word[1]
    gender = word[2]
    base = blend(nominative, genitive, gender)

    if nominative in hack_nouns.keys():
        return hack_nouns[nominative]

    

    if declension == Suf.D6:
        #Imparisyllaba:
        #If declension is III, and genitive is in -is,
        #followed by consonant group, then use given
        #*full* genitive to derive the base.
        #
        #The above [:-2], etc. should *not* be replaced
        #with .split()!
        #check again for -s and -er
        if (nominative.endswith("s") or nominative.endswith("er")):
            if is_consgroup(genitive[:-2]):
                if is_fullgen(nominative,genitive):
                    return genitive[:-2]
                else:
                    return base[:-2]
            else:
                if is_fullgen(nominative, genitive):
                    #Ie: princeps,principis,m
                    #where genitive is whole word.
                    return genitive[:-2]
                else:
                    #TODO -Important!
                    # add support for parisyllaba nouns (civis,civis)
                    return nominative[:-2]
        
        
    if declension == Suf.Gr:
        if nominative[-2:] in ("es", "as"):
            return nominative[:-2]
        if genitive == "e":
            return nominative[:-1]
        

    if declension == Suf.D1:
        return nominative[:-1] #1st dec ie. puella, -ae

  
    elif declension == Suf.D2:
        if nominative.endswith("us"):
            return nominative[:-2] #2nd dec ie. lupus, -i
        #What follows is correction for "fleeting e":
        if nominative.endswith("er"):
            return fleetinge(nominative, genitive)
        if nominative in keepe_II:
            return nominative
        
    elif declension == Suf.D3:
        return nominative[:-2] #2nd dec. ie. bellum, -i (n)

    
    # Third declension ----------------------------->
    elif declension == Suf.D4:
        if nominative[-1] == "x":
            # from gen -is (subgroup of III dec.)
            return genitive[:-2]
        elif genitive.endswith("inis") and not is_fullgen(nominative, genitive):
            return base[:-2]
        elif genitive.endswith("atis") and not is_fullgen(nominative, genitive):
            return base[:-2]
        elif genitive.endswith("oris") and not is_fullgen(nominative, genitive):
            return base[:-2]
        else:
            return genitive[:-2]        

        
    elif declension == Suf.D5 or declension == Suf.D5a:
        #What follows is correction for "fleeting e":
        if nominative.endswith("er"):
            return fleetinge(nominative, genitive)
        else:
            return base[:-2]        

        
    elif declension == Suf.D6 or declension == Suf.D6a:
        if nominative.endswith("e"):
            return nominative[:-1]
        else:
            return base[:-2]

    # Third declension end-------------------------->
    
    elif declension == Suf.D7:
        return base[:-2]
    
    elif declension == Suf.D8:
        return nominative[:-1]
    
    elif declension == Suf.D9:
        return nominative[:-2]

    else:
        raise NoStemError

def fleetinge(nominative, genitive):
    #What follows is correction for "fleeting e":
    if nominative.endswith("er"):
        if genitive.endswith("eri") or genitive=="i":
            return nominative
        else:
            return nominative[:-2] + "r"


def blend(nom, gen, gd):
    """
    Blend nominative and genitive.
    Blends nominativus and genitivus (dictionary entries) to get genitive
    form. Ie: palus,udis returns paludis.
    """
    # First, check if full genitive is already present:
    if is_fullgen(nom, gen):
        return gen
    
    # These are different nominative and genitive
    # endings and rules for making stem to which
    # derivative endings (strings in Dx) will be added
    if nom.endswith("es") and gen == "ae": #Greek dec.
        return "%s%s" % (nom[:-2], gen)
    if nom.endswith("e") and gen == "ae":  #Greek dec.
        return "%s%s" % (nom[:-1], gen)
    if nom.endswith("as") and gen == "ae": #Greek dec.
        return "%s%s" % (nom[:-2], gen)
    if nom.endswith("us") and gen == "oris":
        return "%s%s" % (nom[:-2], gen)
    if nom.endswith("es") and (gen == "itis" or gen == "is"):
        return "%s%s" % (nom[:-2], gen)
    if nom.endswith("en") and gen == "inis":
        return "%s%s" % (nom[:-2], gen)
    if nom.endswith("t") and gen == "itis":
        return "%s%s" % (nom[:-2], gen)
    if nom.endswith("us") and gen == "eris":
        return "%s%s" % (nom[:-2], gen)
    if nom.endswith("ur") and gen == "oris":
        return "%s%s" % (nom[:-2], gen)
    if nom.endswith("us") and gen == "udis":
        return "%s%s" % (nom[:-2], "udis")
    if nom.endswith("us") and gen == "utis":
        return "%s%s" % (nom[:-2], "utis")
    if nom.endswith("al") or nom.endswith("ar") and gen == "is":
        return nom
    if nom.endswith("e") and gen == "is":
        return nom[:-1]
    if gen.endswith("inis"):
        # homo, inis, m
        # origo, ginis, f
        nt = nom[:-1]
        if nt.endswith(gen[:1]):
            return "%s%s" % (nom[:-1], gen[1:])
        else:    
            return "%s%s" % (nom[:-1], gen)
    #if nom.endswith("s") and gen.endswith("is"):
    if gen.endswith("is"):
        # Examples of possible entries:
        #  1) princeps,principis
        #  2) princeps, cipis
        if is_fullgen(nom, gen):
            return gen
        else:
            return blend_third(nom, gen)
    if nom.endswith("t") and gen.endswith("itis"):
        #ie. caput,capitis,n
        # TODO: check is above check for -t,-itis has any sense
        return gen
    if nom.endswith("x") and gen.endswith("is"):
        #example: rex,regis; dux,ducis.
        return gen

    #raise BlendingError
    
    # I forgot to comment and I do not know what's the thing
    #below, but I guess it deals with all other cases.
    w1 = nom[0:-1]
    if w1[-1] == gen[0]:
        bln = "%s%s" % (w1[0:-1], gen)
    else:
        bln = "%s%s" % (w1, gen)
    return bln

def blend_third(nom, gen):
    "Combine nom & gen of III dec."
    #fast, bad solution because not
    #all nouns fit: TODO: rewrite this.
    nom = nom[:-2]
    return "%s%s" % (nom, gen)
        

def is_fullgen(nom, gen, n=2):
    """
    True if full genitive is provided.
    Cheap solution that does not consider
    possible exceptions: assumes that
    nominative and genitive shoud have
    same firts 2 (by default) letters.""" 
    if nom[:n] == gen[:n]:
        return True
    else:
        if gen in ('oris'):
            return True
        else:
            return False
    

def fdec(word):
    """
    Identify declension.
    Identify noun's declension ID (named set of prefixes D1, D2...etc).
    Finds declension of the word. Requires tuple or list as input.

    Example:

    >>> fdec(['nomen', 'inis', 'n'])
    (('', 'is', 'i', '', '', 'e', 'a', 'um', 'ibus', 'a', 'a', 'ibus'),
    'dec003b')
    """
    nominative = word[0]
    genitive = word[1]
    gender = word[2]
    # Isolated leters form word[].
    # This is needed for further checking.
    lt3 = nominative[len(word[0])-3:]
    lt2 = nominative[len(word[0])-2:]
    lt1 = nominative[len(word[0])-1:]
    # Joined boolean queries. The aim is to
    # conclude to which declension noun
    # belongs; this is done in "if" block
    # bellow.
    #                                                  was 'es' & 's':
    is_third_1 = (lt2 == "or"  or lt1=="x"\
                  or lt2 == "do" or lt2 == "us" or lt2 == "go" \
                  or lt2 == "as") or  lt1 == "o"
    # 2 is for consonant base neutrum, III dec. (p. 50)
    is_third_2 = (lt3 == "men" or lt2 == "us" or lt2 == "ur" \
                  or lt1 == "t" or genitive.endswith('oris'))
    is_third_3 = (lt2=="is" or lt2=="es" or lt2=="er" or lt1=="s")
    is_third_4 = (lt2 == "al" or lt2 == "ar" or lt1 == "e")
    
    # Find noun's declension based on following data:
    # nominative, nominative ending, genitive ending
    # and gender.

    if nominative == "":
        raise WordListFormatError
    #Correction for II with fleeting "e":
    if nominative.endswith("er") and genitive.endswith("i"):
        return Suf.D2, "dec002c"
    #Correction for III with fleeting "e":
    if nominative in ("pater", "mater", "frater"):
        return Suf.D5a, "dec003elusive"
    #Guess the declension:
    # Greek dec.
    #TODO: Pay more attention to the Greek dec.
    if genitive.endswith("es"):
        return Suf.Gr, "decGr"
    if genitive.endswith("ae") and (nominative.endswith("ias") \
                        or nominative.endswith("es") \
                        or nominative.endswith("phe")):
        return Suf.Gr, "decGr"
    # end of Greek declension
    if genitive.endswith("ae") and (gender == "f" \
                         or gender == "m"):      # 1st
        return Suf.D1, "dec001"
    elif genitive.endswith("i") and gender == "m":     # 2nd
        return Suf.D2, "dec002a"
    elif genitive.endswith("i") and gender == "n":     # 2nd
        return Suf.D3, "dec002b"
    elif genitive.endswith("is"):               # 3rd
        if is_third_1 == True and (gender=="m" or gender=="f"):
            return Suf.D4, "dec003a"
        elif is_third_2 == True and gender=="n":
            return Suf.D5, "dec003b"
        elif is_third_3:
            return Suf.D6, "dec003c"
        elif is_third_4:
            return Suf.D6a, "dec003d"
        else:
            #Let's assume it's the type with zero nominal ending,
            #because we came all the way through if-blocks, and
            #hope it's OK. Example of the noun: consul,-is
            return Suf.D6,"dec003c by exclusion"
    elif genitive.endswith("us"): #4th
        if gender == "m":
            return Suf.D7, "dec004a"
        elif gender == "n":
            return Suf.D8, "dec004b"
        else:
            raise GenderError
    elif genitive.endswith("ei"):  #5th
        return Suf.D9, "dec005"
    else:
        try:
            raise ToDo_CodeGoesHere, "try to guess form of the noun"
        except:
            raise CannotSetDeclensionError

def guess(word):
    "TODO: try to guess genitive and gender"
    raise "We don't sell that cheese."
