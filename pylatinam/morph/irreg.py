#! /usr/bin/python
"""Irregular forms

Useful links:
http://www.orbilat.com/Languages/Latin/Grammar/Latin-Declension_3rd.html
http://en.wiktionary.org/wiki/vis#Latin

"""

__author__= "mlinar"
__url__ = "http://www.pylatinam.com/"
__mail__ = "cheesepy [a] gmail.com"
__version__="0.0.1"

irreg_nom = {'vis,vis,f':(('vis','vis','vi','vim','vis','vi', \
             'vires','virium','viribus','vires','vires','viribus'),\
             'dec03irreg', 'irreg', 'vi|vir'),
             # ----------------
             'bos,bovis,m':(('bos','bovis','bovi','bovem','bos','bove', \
             'boves','boum','bobus|bubus','boves','boves','bobus|bubus'),\
             'dec03irreg', 'irreg', 'bov|bou|bub'),
             'bos,bovis,f':(('bos','bovis','bovi','bovem','bos','bove', \
             'boves','boum','bobus|bubus','boves','boves','bobus|bubus'),\
             'dec03irreg', 'irreg', 'bov|bou|bub'),
             # ----------------
             'sus,suis,m':(('sus','suis|sueris','sui','suem','sus','sue', \
             'sues','suum','subus|suibus','sues','sues','subus|suibus'),\
             'dec03irreg', 'irreg', 'su|sui'),
             'sus,suis,f':(('sus','suis|sueris','sui','suem','sus','sue', \
             'sues','suum','subus|suibus','sues','sues','subus|suibus'),\
             'dec03irreg', 'irreg', 'su|sui'),
             'sus,sueris,f':(('sus','suis|sueris','sui','suem','sus','sue', \
             'sues','suum','subus|suibus','sues','sues','subus|suibus'),\
             'dec03irreg', 'irreg', 'su|sui'),
             'sus,sueris,m':(('sus','suis|sueris','sui','suem','sus','sue', \
             'sues','suum','subus|suibus','sues','sues','subus|suibus'),\
             'dec03irreg', 'irreg', 'su|sui'),
             # ----------------
             'juppiter,jovis,m':(('Juppiter','Jovis','Jovi','Jovem','Jupiter','Jove', \
             '','','','','',''),\
             'dec03irreg', 'irreg', 'jov')}

