#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 11:32:45 2019

@author: rosto
"""

class Builder():
    def __init__(self, obj_html_root):
        self.DATI = {
            "HEAD":"""<meta charset="utf-8">
                    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
                    """,
            "SCRIPT":"""<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>""",
            "TITOLO":"",
            "DESCRIZIONE":"",
            "BODY":""
            }
        #
        self.ogg_html_radice = obj_html_root
        self.SCHELETRO: str = (
            """
<!doctype html>

<html lang="it">
<head>
  {HEAD}  

  <title>{TITOLO}</title>
  <meta name="description" content="{DESCRIZIONE}">

</head>

<body>
  {BODY}
  {SCRIPT}
</body>
</html>
"""
            )
    
    def __str__(self):
        self.DATI["BODY"] = self.ogg_html_radice.to_html()
        return self.SCHELETRO.format(**self.DATI)
    
    def imposta_titolo(self, titolo: str) -> None:
        self.DATI["TITOLO"] = titolo
    
    def aggiungi_script(self, riga: str) -> None:
        self.DATI["HEAD"] += riga
    
    def aggiungi_head(self, riga: str) -> None:
        self.DATI["SCRIPT"] += riga
    
    def aggiungi_file_javascript(self, file: str) -> None:
        self.DATI["SCRIPT"] += """<script src="%s"></script>""" % (file,)
    
    def aggiungi_codice_javascript(self, codice: str) -> None:
        self.DATI["SCRIPT"] += """<script type="text/javascript">%s</script>""" % (codice,)
