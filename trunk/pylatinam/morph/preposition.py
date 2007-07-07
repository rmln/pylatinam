"""Prepositions (package pyLatinam)

This class deals with prepositions. It has one class (Prep()) that
calls Lex() to find prepostition in lexicon, together with congruence
markers.


Congruence markers and nominal

Each preposition in lexicon has number that refers to the case
preposition goes with. Class Prep() calls function congru_nom_prep()
and returns cases of nominal, provided nominal is passed to the class.
Congruency cases are stored in Prep().congru and contains two
dictionaries, Prep().congru[0] for singular and Prep().congru[1] for
plural nominals.

Example:

>>> prep = Prep("in", "bellum")
>>> prep.entry
'in'
>>> prep.translate
[['in', 'in', 'on', 'against', 'to']]
>>> prep.congru
({3: 'bellum', 5: 'bello'}, {8: 'bellis', 10: 'bella'})
>>> prep.congru_id
['3', '5']
"""

__author__= "miller"
__mail__ = "cheesepy@gmail.com"
__version__="0.4"


# Import exception relevant to this
# module only:

from latinam.ltexcept import NoPrepCongruIdError

from latinam.lexicon.lexicon import Lex
from noun import Nom

class Prep:
    """Creates class for prepsition (with congruence)
    
    """

    __name__ = "Prep"
    
    def __init__(self, word, nominal=None):
        """Creates preposition"""
        self.congru = None
        self.nominal = nominal
        prep = Lex(word, pos="prep")
        self.translate = prep.lookup
        self.entry = prep.entry[0]
        prep.entry.__delitem__(0)
        self.congru_id = prep.entry
    def do_congru(self):
        """do conguence"""
        if len(self.congru_id)==0:
            raise NoPrepCongruIdError
        if not self.nominal==None:
            self.congru = congru_nom_prep(self.congru_id, self.nominal)

def congru_nom_prep(congru_id, nominal):
    """Find congruence for given preposition and nominal"""
    nominal_cases = Nom(nominal)
    congru = ({},{})
    for item in congru_id:
        item = int(item)
        congru[0][item]=nominal_cases.casii[item]
        congru[1][item+5]=nominal_cases.casii[item+5]
    return congru
