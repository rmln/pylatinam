#! /usr/bin/python
"""Adjectives

Adjectives
==========

This file contains classes and functions that deal with declensions
of adjectives.

Adj() - class with adjectival attributes
----------------------------------------

If no gender reference is provided, the class will return adjective
declension for given adjective.

If gender reference is provided class will return no more than two
declensions (two for masc. and one for fem/neut).

Value gen="mfn" will return all forms of adjective.

Switches for getting gradation:

grade="comp"; grade="sup"; grade="full"

The last will return both comparative and superlative:

>>> (('clarior', 'clarius', None), ('clarissimus', 'clarissima', 'clarissimum'))
    
"""

__author__= "mlinar"
__url__ = "http://latin.languagebits.com/"
__mail__ = "cheesepy [a] gmail.com"
__version__="0.0.5"


from strings import NomStr
from strings import AdjStr
from noun import Nom

from pylatinam.pylatexcept import \
    ItemNumberError, NoStemError, \
    WordListFormatError, GenderError, \
    CannotSetDeclensionError, InvalidGenitiveCompError, \
    InvalidComparationIDError
    

from pylatinam.lexicon.lexicon import Lex

Suf = NomStr()
Adjs = AdjStr()

class Adj:
    """
    Class with adjectival attributes
    """
    __name__ = "Adj"
    def __init__(self, word, gender="m", grade="full"):
        adj_mfn = adj_genitive(word, gender=gender)
        casii = []
        self.type = []
        self.translate = []
        self.entry = word
        try:
            lex = Lex(nword, pos=pos)
            self.translate = lex.lookup
        except: pass
        Nomc = Nom
        for item in adj_mfn:
            if item==None:
                break
            classcall = Nomc(item, pos="adj", nolex=True)
            casii.append(classcall.casii)
            self.type.append(classcall.type)
        self.casii = casii
        self.pos = "adj"
        self.gender = gender
        #comparation:
        self.comp = adj_comp(casii[0][1], grade=grade)

class Adjf(Adj):
    """bypass Adj() class with gender='mfn' value"""
    def __init__(self, word):
        Adj.__init__(self, word, grade="full", gender="mfn")


def adj_comp(genitive, grade="comp"):
    """Create comparative and cases
    Comparative:
    carus, -i --> car-
        car-ior     (m & f)
        car-ius     (n)
            Declension: NomStr.adj
    Superlative (m,f,n):
        car-issimus
        car-issima
        car-issimum
    """
    if not genitive.endswith("i" or "is"):
        raise InvalidGenitiveCompError
    else:
        if genitive.endswith("i"):
            base = genitive.strip("i")
        else:
            base = genitive.strip("is")
    if grade in ("comp", "sup", "full"):
        if grade == "comp": return grade_comp(base)
        if grade == "sup": return grade_sup(base)
        if grade == "full": return grade_full(base)
    else:
        raise InvalidComparationIDError

def grade_comp(base):
    """Return comparative for entered base"""
    return base + "ior", base + "ius", None

def grade_sup(base):
    """Return superlative for entered base"""
    base = base + "issim"
    return base + "us", base + "a", base + "um"

def grade_full(base):
    """Return comparative and superlative for entered base"""
    return (grade_comp(base), grade_sup(base))
        
def adj_genitive(adjective, gender=None):
    """
    Returns all genders of adjective.
    
    This is done by comparing and matching values in
    StrAdj().nomgen. Example:

    >>> adj_genitive("carus", gender="mfn")
        [('carus', 'i', 'm'), ('carer', 'i', 'm'),
        ('cara', 'ae', 'f'), ('carum', 'i', 'n')]
    """
    adj_nom_gen = Adjs.nomgen #nominative and genitive endings
    adj_mfn = []
    tmp = []
    for item in adj_nom_gen:
        if adjective.endswith(item[0]):
             base = adjective.strip(item[0])
             original = adjective, item[1], item[2]
             tmp.append(original)
             tmp.append(None)
             
    for item in adj_nom_gen:
        adj_mfn.append(('%s%s' % (base, item[0]),item[1],item[2]))
    
    #add error routine
    if gender=="mfn":
        return adj_mfn
    elif gender==None:
        return tmp
    elif gender=="m":
        return adj_mfn[0],adj_mfn[1]
    elif gender=="f":
        tmp.append(adj_mfn[2])
        tmp.append(None)
        return tmp
    elif gender=="n":
        tmp.append(adj_mfn[3])
        tmp.append(None)
        return tmp
