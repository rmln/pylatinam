#! /usr/bin/python
"""Irregular auxiliary verb forms


"""

__author__= "mlinar"
__url__ = "http://www.pylatinam.com/"
__mail__ = "cheesepy [a] gmail.com"
__version__="0.0.2"

class Esse:
    """Sum, esse, fui

    Good online overview:

    http://www.math.ohio-state.edu/~econrad/lang/lvesse.html

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
        #
        self.ind_fu = 'ero', 'eris', 'erit', 'erimus', 'eritis', 'erunt'
        #
        self.sub_pr = 'sim', 'sis', 'sit', 'simus', 'sitis', 'sint'
        self.sub_im = 'essem', 'esses', 'esset', 'essemus', 'essetis', 'essent'
        self.sub_pe = 'fuerim', 'fueris', 'fuerit', 'fuerimus', 'fueritis', 'fuerint'
        self.sub_pl = 'fuissem', 'fuisses', 'fuisset', 'fuissemus', 'fuissetis', 'fuissent'
    
