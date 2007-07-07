tnhead = """
NOUN DECLENSION - OUTPUT
----------------------------------------------------------------------
This is an output of declension created by Python program pyLatinam.

Created by uot.py (latinam.tools), class OutLatinam via attributte
show(detail=0).

Versions:

    Nom class                %s
    Latinam package          %s
    Out module               %s

"""

tvhead = """
VERB CONJUGATION - OUTPUT
----------------------------------------------------------------------
This is an output of conjugation created by Python program pyLatinam.

Created by uot.py (latinam.tools), class OutLatinam via attributte
show(detail=0).

Versions:

    Ver class                %s
    Latinam package          %s
    Out module               %s

%s

"""

head = '''
<!doctype html PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html><head><title>pyLatinam: %s</title>
<META content="pyLatinam.tools.OutLatinam 0.4" name=GENERATOR>
</head><body bgcolor="#f0f0f8">
'''

nountable = '''

                <table width="500" border="0" cellpadding="1" cellspacing="0">
                  <tr> 
                    <td width="41"> 
                      <div align="center">c/n</div>
                    </td>
                    <td width="203" bgcolor="#CCCCFF"> 
                      <div align="center">Sigular</div>
                    </td>
                    <td width="234" bgcolor="#CCCCFF"> 
                      <div align="center">Plural</div>
                    </td>
                  </tr>
                  <tr> 
                    <td width="41" bgcolor="#6699FF"> 
                      <div align="center">Nom.</div>
                    </td>
                    <td width="203"><font size="2" face="Courier New, Courier, mono">%s</font></td>
                    <td width="234"><font size="2" face="Courier New, Courier, mono">%s</font></td>
                  </tr>
                  <tr> 
                    <td width="41" bgcolor="#6699FF"> 
                      <div align="center">Ged.</div>
                    </td>
                    <td width="203"><font size="2" face="Courier New, Courier, mono">%s</font></td>
                    <td width="234"><font size="2" face="Courier New, Courier, mono">%s</font></td>
                  </tr>
                  <tr> 
                    <td width="41" bgcolor="#6699FF"> 
                      <div align="center">Dat.</div>
                    </td>
                    <td width="203"><font size="2" face="Courier New, Courier, mono">%s</font></td>
                    <td width="234"><font size="2" face="Courier New, Courier, mono">%s</font></td>
                  </tr>
                  <tr> 
                    <td width="41" bgcolor="#6699FF"> 
                      <div align="center">Acc.</div>
                    </td>
                    <td width="203"><font size="2" face="Courier New, Courier, mono">%s</font></td>
                    <td width="234"><font size="2" face="Courier New, Courier, mono">%s</font></td>
                  </tr>
                  <tr> 
                    <td width="41" bgcolor="#6699FF"> 
                      <div align="center">Voc.</div>
                    </td>
                    <td width="203"><font size="2" face="Courier New, Courier, mono">%s</font></td>
                    <td width="234"><font size="2" face="Courier New, Courier, mono">%s</font></td>
                  </tr>
                  <tr> 
                    <td width="41" bgcolor="#6699FF"> 
                      <div align="center">Abl.</div>
                    </td>
                    <td width="203"><font size="2" face="Courier New, Courier, mono">%s</font></td>
                    <td width="234"><font size="2" face="Courier New, Courier, mono">%s</font></td>
                  </tr>
                </table>
                <hr width="500" align="left">
'''

erinfo = '''
<p>The program generated error while processing the following:</p>
'''

ending = '''
<p>End of the list.</p>
<p><i>Inflexions and file generated by pyLatinam</i></p>
</body>
</html>
'''
