#! /usr/bin/python
"""pyLatinam - Automated Latin Grammar

About pyLatinam
===============

The easiest way to think of this program is to imagine an
automated grammar. The user can provide basic forms of words
(nominative case or infinitive) and the program will produce the
declension or verbal forms.

In essence, pyLatinam deals with declension, conjugation and analysis
of Latin words. Please note that this is an incomplete software in planning
phase. The work on it is not constant, though the project is alive and
new releases and improvements are to come.

If you are wondering why this program exists, well, the answer is:
curiosity. I'm an amateur programmer who likes languages. But to be honest, 
I am not knowledgeable about Latin - I had it two years in high-school. 

However, Latin seemed good as a start for experimenting with
linguistics and programming.

The project is growing bigger and complex, but every module, class and
some functions are documented. In future releases even more attention will
be paid to documentation.

Please don't expect to have clear and grammatically correct outputs
for every input in this phase of the project: there are many, many 
grammatical rules left to implement. The fact that this program is
about native language should indicate how tricky things can be.


Exploring the content
=====================

There are two to get outputs. These are:

 - Console
 - Online web version (recommended to most users)


Console
-------

>>> import latinam as lt
>>> lt.Nom("puella").show()

The above will list all cases of noun "girl" in Latin. Notice that this
word has to be defined in the lexicon (see /lexicon directory). However,
you can tell program to use you entry and ignore the lexicon:

>>> lf.Nom("puella,ae,f",nolex=True)

Or:

>>> lf.Nomf("puella,ae,f")

As you can see, the input is different. Please refer to documentation for
details.


Online WEB version
------------------

Point your browser to http://www.pylatinam.com/ for an introduction or 
visit the interactive pages directly:

U{http://www.pylatinam.com/interactive/}

Web version 'evolved' from small debugging tool. It is suitable for
users who want simple and functional overview of pyLatinam.

API Documentation
-----------------

Available on U{http://www.pylatinam.com/api/}

The Code & Technical Info
-------------------------

U{http://code.google.com/p/pylatinam/}

Blog
----

U{http://blog.proprevod.com/?tag=pylatinam}

Contacting the Author
---------------------

Mail:

cheesepy [a] gmail.com

Feedback is welcome!

Legal
-----

pyLatinam is an open-source program for personal and/or educational 
non-commercial use. It is published under New BSD License.


"""

__author__= "mlinar"
__url__ = 'http://www.pylatinam.com/'
__mail__ = "cheesepy [a] gmail.com"
__version__="0.1.9"

import pylatexcept
import lexicon
import morph
import syntax
import tools
from locals import *

def versions():
    "Versions of pylatinam modules"
    return {
        "pylatinam":__version__,
        "noun":morph.noun.__version__,
        "verb":morph.verb.__version__,
        }
