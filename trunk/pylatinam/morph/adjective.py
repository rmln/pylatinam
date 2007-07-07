"""Adjectives

This file contains classes and functions that deal with declensions
of adjectives.

Adj()

Class with adjectival attributes

If no gender reference is provided, the class will return adjective
declension for given adjective.

Value gen="mfn" will return all forms of adjective.

If gender reference is provided class will return no more than two
declensions (two for masc. and one for fem/neut).
    
"""

__author__= "miller"
__mail__ = "cheesepy@gmail.com"
__version__="0.5"


from strings import NomStr, AdjStr
from noun import Nom

from latinam.ltexcept import \
    ItemNumberError, NoStemError, \
    WordListFormatError, GenderError, \
    CannotSetDeclensionError, InvalidGenitiveCompError, \
    InvalidComparationIDError
    

from latinam.lexicon.lexicon import Lex

Suf = NomStr()
Adjs = AdjStr()

class Adj:
    """
    Class with adjectival attributes
    """
    __name__ = "Adj"
    def __init__(self, word, gender="m", grad=None):
        adj_mfn = adj_genitive(word, gender=gender)
        casii = []
        self.type = []
        Nomc = Nom
        for item in adj_mfn:
            if item==None:
                break
            classcall = Nomc(item, pos="adj", nolex=True)
            casii.append(classcall.casii)
            self.type.append(classcall.type)
        self.casii = casii
        self.pos = "adj"
        #comparation:
        self.comp = None
        if grad != None:
            self.comp = adj_comp(casii[0][1], grad)
            


class Adjf(Adj):
    """bypass Adj() class with gender='mfn' value"""
    def __init__(self, word):
        Adj.__init__(self, word, grad=None, gender="mfn")


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
    if grade == "comp":
        return base + "ior", base + "ius", None
    elif grade == "sup":
        base = base + "issim"
        return base + "us", base + "a", base + "um"
    else:
        raise InvalidComparationIDError
    

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
    #pass
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
