"""XML outputs

XML outputs
===========

This module creates XML for entered morphology element. When initialised
with morph class (ie. Nom(), Ver(), Adj()) the class Latxml will create
XML document for given part of speech.

Notes:

 - XML document is in Latxml().e_nom element.
 - For now function supports nouns and verbs

In: Morphology class

Out: DOM object

Example:

>>> from latinam import Nom
>>> nom = Nom("lupus")
>>> xml = Latxml(nom)
>>> xml.e_nom.toprettyxm
>>> print xml.e_nom.toprettyxml()

Results in::

    <nom>
            <entry>
                    lupus, i, m
            </entry>
            <stem>
                    lup
            </stem>
            <suf>
                    us, i, o, um, e, o, i, orum, is, os, i, is
            </suf>
            <translate>
                    
            </translate>
            <type>
                    dec002a
            </type>
            <casii>
                    <nom_s>
                            lupus
                    </nom_s>
                    <gen_s>
                            lupi
                    </gen_s>
                    <dat_s>
                            lupo
                    </dat_s>
                    <acc_s>
                            lupum
                    </acc_s>
                    <voc_s>
                            lupe
                    </voc_s>
                    <abl_s>
                            lupo
                    </abl_s>
                    <nom_p>
                            lupi
                    </nom_p>
                    <gen_p>
                            luporum
                    </gen_p>
                    <dat_p>
                            lupis
                    </dat_p>
                    <acc_p>
                            lupos
                    </acc_p>
                    <voc_p>
                            lupi
                    </voc_p>
                    <abl_p>
                            lupis
                    </abl_p>
            </casii>
    </nom>


"""

from xml.dom.minidom import Document

__author__= "mlinar"
__url__ = "http://latin.languagebits.com/"
__mail__ = "cheesepy [a] gmail.com"
__version__ = "0.1"

#from pylatinam import Nom
#nom = Nom("lupus")

from pylatinam import Ver
from pylatinam.morph.strings import vkeys

#ver = Ver("amo")

class Latxml:

    def __init__(self, lclass):
        """Creates XML document for nouns"""
        run = getattr(self, "xml_%s" % lclass.__name__)
        run(lclass)
        
    def xml_Nom(self, lclass):
        "make it simple"
        doc = Document()
        # Root element <nom>
        e_nom = doc.createElement("nom")
        e_nom.setAttribute("nolex", str(lclass.nolex))
        doc.appendChild(e_nom)
        # info about noun
        elements = "entry", "stem", "suf", "translate", "type"
        require_formating = "entry", "suf"
        for item in elements:
            #what shall we add as text?
            text = getattr(lclass, item)
            if item in require_formating:
                text = ", ".join(text)
            else:
                text = str(text)
            e_item = doc.createElement(item)
            e_item.appendChild(doc.createTextNode(text))
            e_nom.appendChild(e_item)
        #element for "casii"
        e_casii = doc.createElement("casii")
        e_nom.appendChild(e_casii)
        # Declension
        # these are strings for creating case's nods in xml:
        cases = "nom_%s", "gen_%s", "dat_%s", "acc_%s", "voc_%s", "abl_%s"
        # fetch cases from class:
        casii = getattr(lclass, "casii")
        for item in range(12):
            # we have plural and singular, but 12 elements;
            # this is where we separate it - if i < 6 then it's
            # singular, otherwise plural.
            if item < 6:
                suf = "s"
                case_string_id = item
            else:
                case_string_id = item - 6
                suf = "p"
            text = casii[item]
            # creation of elements;
            case = cases[case_string_id] % suf
            e_item = doc.createElement(str(case))
            e_item.appendChild(doc.createTextNode(text))
            e_casii.appendChild(e_item)

        #make this publicaly available:
        self.e_nom = e_nom
        self.doc = doc

    def xml_Ver(self, lclass):
        """Creates XML document for verbs"""
        # define elements and subelements:
        #from strings import vkeys
        in_tenses = vkeys      
        doc = Document()
        e_ver = doc.createElement("ver")
        doc.appendChild(e_ver)
        # entry
        e_entry = self.do_populate("entry", lclass, 1)
        e_ver.appendChild(e_entry)
        # translation
        e_translate = self.do_populate("translate", lclass)
        e_ver.appendChild(e_translate)
        # morph
        e_morph = self.do_populate("morph", lclass.morph)
        e_ver.appendChild(e_morph)
        # tenses
        e_tenses = self.do_populate("tenses", lclass.tenses, 1)
        e_ver.appendChild(e_tenses)
        # tenses
        e_participle = self.do_populate("participle", lclass.participle, 1)
        e_ver.appendChild(e_participle)
        # the result:
        self.e_ver = e_ver
        self.doc = doc

    def do_populate(self, name, entry, format=0, exclude=[]):
        "create xml node based on entry"
        doc = Document()
        nod = doc.createElement(name)
        if isinstance(entry, dict):
            for item in entry.keys():
                if item not in exclude:
                    e_item = doc.createElement(item)
                    #format strings
                    text = entry[item]
                    if format:
                        if len(text) == 2 and isinstance(text[0], list):
                            text = ["%s %s" % (text[0][x],text[1][x]) for x in range(6)]
                        text = ", ".join(text)
                    else:
                        text = str(text)
                    e_item.appendChild(doc.createTextNode(text))
                    nod.appendChild(e_item)
            return nod
        else:
            e_item = doc.createElement(name)
            text = str(getattr(entry, name))
            e_item.appendChild(doc.createTextNode(text))
            return e_item
        

        
        
    
#n = Latxml(nom)
#v = Latxml(ver)
#print n.e_nom.toprettyxml()
#print n.doc.toprettyxml()
