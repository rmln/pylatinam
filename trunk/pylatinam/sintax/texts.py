emerald_txt = """
Verum, sine mendacio, certum, et verissimum: Quod est inferious est sicut quod est superius, et quod est superius est sicut quod est inferius, ad perpetranda miracula rei unius. Et sicut res omnes fuerunt ab uno, meditatione unius, sic omnes res natae ab hac una re, adaptatione. Pater eius est sol; mater eius est luna. Portavit illud ventus in ventre suo; nutrix ius terra est. Pater omnis telesmi totius mundi est hic. Virtus eius integra est, si versa fuerit in terram. Separabis terram ab igne, subtile ab pisso, suaviter, magno cum ingenio. Ascendit a terra in coelum, iterumque descendit in terram, et recipit vim superiorum et inferiorum. Sic habebis gloriam totius mundi. Ideo fugiet a te omnis obscuritas. Haec est totius fortitudinis fortitudo fortis, quia vincet omnem rem subtilem, omnemque solidam penetrabit. Sic mundus creatus est. Hinc erunt adaptationes mirabiles, quarum modus est his. Itaque vocatus sum Hermes Trismegistus, habens tres partes philosophiae totius mundi. Completum est quod dixi de operatione solis.
"""

puella_txt = """
Puella est discipula. Puella est impigra. Puella tebellam spectat. Tabula picta puellae pulchra est. Magistra puellae tabellam dat. Puellam pulchram spectas. Puella, pulchra es. Puella comam vitta ornat."""

emerald = {"text":emerald_txt, "id":"emerald", "name":"The Emerald Tablet of Hermes", "lng":"lt"}
puella1 = {"text":puella_txt, "id":"puella1", "name":"Prvo vezbanje: Latiski I", "lng":"lt"}



if __name__=="__main__":
    print emerald["name"], "\n", emerald["text"]
    print puella1["name"], "\n", puella1["text"]
    print "\n\n(From file latinam.sintax.texts.py)"
