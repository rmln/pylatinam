"""Out.py - Latinam

Various output results, mostly for testing.

Usage:

OutLatinam(pos,format,path)

Where arguments are:

    pos         part of speech:
                    n - nouns
                    v - verbs

    format      output file format
                    txt - text
                    html - hypertext

    path        directory for output file; please include
                character for path at the end (\ or /). 
		Leave blank and file will be created in dir
		ectory of this module.

Examples:

To create html page in current directory for
nouns in lexicon file:

>>> OutLatinam("n", "html")
<__main__.OutLatinam instance at 0x016A74B8>

To create txt file for verbs:

>>> OutLatinam("v", "txt")
<__main__.OutLatinam instance at 0x016BB7B0>
"""

__author__= "miller"
__mail__ = "cheesepy@gmail.com"
__version__ = "0.4.2"


import sys
import latinam
from latinam.morph.noun import Nom
from latinam.morph.verb import Ver
from latinam.lexicon.lexicon import LexFind

__formats__ = {"txt":"Plain text", "html":"Hyperlink text"}

__pos__ = {"n":("Nouns", Nom), "v":("Verbs", Ver)}

#lines of text used in output files;
from htmltxt import tnhead, tvhead

ALPH = ("a","b","c","d","e","f","g","h",
        "i","j","k","l","m","n","o","p",
        "q","s","t","u","v","x","y","x")

#text to be added at the beginning of file for NOUNS;
ntext = tnhead % (latinam.morph.noun.__version__,
       latinam.__version__,
       "0.1")


#text to be added at the beginning of file for VERBS;
vtext = tvhead % (latinam.morph.verb.__version__,
       latinam.__version__,
       "0.1",
       latinam.morph.verb.tags())

class OutLatinam:
    """Create files with list of inflected words"""
    
    def __init__(self, pos, format="txt", path=None):
        """inititate class"""

        #if path is None, then save into current dir;
        if path == None:
            path = ""
            
        #check if file format and part of speech provided
        #are supported in the currend version of this class;
        #if arguments are listed, then everything is ok;
        if format not in __formats__.keys():
            raise TypeError, "Output format not supported."
        if pos not in __pos__.keys():
            raise TypeError, "Part of speech not supported."
        
        #use key content for file name; 0 is for file name while
        #1 contains class and is used later;
        partofs = __pos__[pos][0]
        fsock = open('%s%s_out.%s' % (path,partofs,format), 'w')
        
        #save state of stout, so things could be set to it after
        #the class finishes;
        saveout = sys.stdout
        
        #override stdout so that print saves text to file;
        sys.stdout = fsock
        
        #create lists of all items availabe in lexicons;
        #
        #TODO: This line of code is not the best solution
        #because it loads *all* lexicon files; this is
        #done in lexicon.Lex() and requires additional
        #work;
        self.words = LexFind().corpus
        
        #sort the list needed;
        self.words[pos].sort()
        
        #instance of morphology classes that are needed for
        #inflexion;
        self.morph = __pos__[pos][1]

        #get function needed and run it;
        function = getattr(self, "do_%s_%s" % (pos, format))
        function()

        #previous settings;
        sys.stdout = saveout
        
        fsock.close()

    def do_n_txt(self):
        "create text output for nouns"
        wrong = []
        print ntext
        print "\n", "Words: ", str(len(self.words["n"]))
        for word in self.words["n"]:
            try:
                self.morph(word, nolex=True).show(detail=1)
            except:
                wrong.append(word)
        print "\n\n", "*"*70
        print "ERRORS FOR WORDS: ", "\n"
        for item in wrong:
            print "*", item

    def do_v_txt(self):
        "create text output for verbs"
        wrong = []
        print vtext
        print "\n", "Words: ", str(len(self.words["v"]))
        for word in self.words["v"]:
            try:
                self.morph(word, nolex=True).show(detail=1)
            except:
                wrong.append(word)
        print "\n\n", "*"*70
        print "ERRORS FOR WORDS: ", "\n"
        for item in wrong:
            print "*", item

    def do_n_html(self):
        """save declension as html"""
        from htmltxt import head, nountable, erinfo, ending
        print head % "Noun declension"
        print '<a name="topofpage">'
        print '<h1>Noun Declension</h1>'
        wrong = []
        has_it = []
        for letter in ALPH:
            print '<a href="#%s">%s</a>' % (letter, letter.upper())
        for word in self.words["n"]:
            w1 = word[0].lower()
            if not w1 in has_it:
                print '''<h2><a name="%s">%s</a></h2>
                <a href="#topofpage">top</a><br>''' % (w1, w1.upper())
                has_it.append(w1)
            print '<a href="#%s">%s</a><br>' % (word, word)
        for word in self.words["n"]:
            try:
                nc = self.morph(word, nolex=True)
                print '''
                <p>Noun: <b>%s<a name="%s"></a></b>
                <a href="#topofpage">top</a><br>
                Translation(s): %s</p>''' % (word, word, nc.translate)
                print nountable % tuple(nc.casii)
            except:
                wrong.append(word)
        print erinfo
        for item in wrong:
            print "%s<br>" % item
        print ending
            

    def do_v_html(self):
        raise "Sorry, HTML output is yet to be implemented."


#if run as module:
if __name__=="__main__":
    print __doc__
