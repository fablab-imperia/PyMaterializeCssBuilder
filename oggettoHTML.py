#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 12:00:29 2019

@author: rosto
"""

from typing import List

class OggettoHTML():
    def __init__(self, nome_tag="div", ID="", classi=[], src="", aggiuntivi: List[str]=[]):
        self.proprieta=(
            {
            "nome_tag":nome_tag,
            "id":ID,
            "classi":classi,
            "src":src,
            "aggiuntivi":aggiuntivi
            }
            )
        
        self.struttura_tag='<{nome_tag} id="{id}" class="{classi}" src="{src}" {aggiuntivi}>%s</{nome_tag}>'
        self.ogg_figli=[]#Devono ereditare da OggettoHTML
    
    def to_html(self) -> str:
        risposta=""
        ogg_conversione = self.proprieta.copy()
        ogg_conversione["classi"] = " ".join(self.proprieta["classi"])
        ogg_conversione["aggiuntivi"] = " ".join(self.proprieta["aggiuntivi"])
        
        risposta= self.struttura_tag.format(**ogg_conversione)
        risposta= risposta.replace('class="" ',"")
        risposta= risposta.replace('id="" ',"")
        risposta= risposta.replace('for="" ',"")
        risposta= risposta.replace('src="" ',"")
        
        ris_figli = ""
        for figlio in self.ogg_figli:
            ris_figli += figlio.to_html()
        
        return risposta % (ris_figli,)
    
    def add_child(self, child_obj):
        self.ogg_figli.append(child_obj)
    
    def add_class(self, classe: str) -> None:
        self.proprieta["classi"].append(str(classe))
    
    def remove_class(self, classe: List[str]) -> None:
        if classe in self.proprieta["classi"]:
            self.proprieta["classi"].remove(classe)
    
    def add_class_list(self, classi: List[str]) -> None:
        self.proprieta+=classi
    
    def __str__(self):
        return self.to_html()