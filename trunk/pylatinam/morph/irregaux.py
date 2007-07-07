"""Irregular auxiliary verb forms - pyLatinam package

This module list classes of irregular verbs; the classes have similar
attributes as verbs.Ver() class - the only difference is that classes
within this module are precompiled.

What follows is one of the first ideas for "solving the "problem" of
irregular verbs and is definitely going to be changed completely.

"""

__author__= "miller"
__mail__ = "cheesepy@gmail.com"
__version__="0.2"

class Esse:
    """Sum, esse, fui --> list of verb inflexions

    Verb esse ("to be"), as in most other languages, shows many
    irregularities. Attributes of Esse() are same as in Ver()
    cllass instances, but are "pre-compiled". In other words,
    class Esse serves as big string dictionary.

    Verb Esse() in package pyLatinam is labeled as "always irregular",
    which means that module latinam.verbs will never compile esse
    forms, but instantiate its forms from this class (although some
    esse forms are regular). Labeling it as "always irregular" makes
    things more straightforward, since there is no need to distinguish
    between regular and irregular forms.
    
    """
    __name__ = "Esse"
    def __init__(self):
        self.imp2 = None,"esto","esto",None,"estote","sunto"
        self.imp1 = None,"es",None,None,"este",None
        self.ipp = "","","","","",""
        self.iperp = "","","","","",""
        self.futa2 = "fuero","fueris","fuerit","fuerimus","fueritis","fuerit"
        self.futa1 = "","","","","",""
        self.iima = "eram","eras","erat","eramus","eratis","erant"
        self.iplu = "fueram","fueras","fuerat","fueramus","fueratis","fuerant"
        self.futp1 = "","","","","",""
        self.iper = "fui","fuisti","fuit","fuimus","fuistis","fuerunt"
        self.ipra = "sum","es","est","sumus","estis","sunt"
    
