#! /usr/bin/python
"""Prepositions

This class deals with prepositions. It has one class (Prep()) that
calls Lex() to find preposition in lexicon, together with congruence
markers.

Congruence markers are id's of cases that go with
the preposition and are stored in .congru attribute.

"""

__author__= "mlinar"
__url__ = "http://latin.languagebits.com/"
__mail__ = "cheesepy [a] gmail.com"
__version__="0.0.2"


# Import exception relevant to this
# module only:

from pylatinam.pylatexcept import NoPrepCongruIdError

from pylatinam.lexicon.lexicon import Lex
from noun import Nom

class Prep:
    """Creates class for prepsition (with congruence markers)
    
    """

    __name__ = "Prep"

    __congru__ = "Nom", "NomPhr", "Adj"
    
    def __init__(self, word):
        """Creates preposition"""
        prep = Lex(word, pos="prep")
        self.translate = prep.lookup
        self.entry = prep.entry[0]
        prep.entry.__delitem__(0)
        self.congru = prep.entry

        
#obsolete:

##class Prep:
##    """Creates class for prepsition (with congruence)
##    
##    """
##
##    __name__ = "Prep"
##    
##    def __init__(self, word, nominal=None):
##        """Creates preposition"""
##        self.congru = None
##        self.nominal = nominal
##        prep = Lex(word, pos="prep")
##        self.translate = prep.lookup
##        self.entry = prep.entry[0]
##        prep.entry.__delitem__(0)
##        self.congru_id = prep.entry
##        
##    def do_congru(self):
##        """do conguence"""
##        if len(self.congru_id)==0:
##            raise NoPrepCongruIdError
##        if not self.nominal==None:
##            self.congru = congru_nom_prep(self.congru_id, self.nominal)
##
##def congru_nom_prep(congru_id, nominal):
##    """Find congruence for given preposition and nominal"""
##    nominal_cases = Nom(nominal)
##    congru = ({},{})
##    for item in congru_id:
##        item = int(item)
##        congru[0][item]=nominal_cases.casii[item]
##        congru[1][item+5]=nominal_cases.casii[item+5]
##    return congru
