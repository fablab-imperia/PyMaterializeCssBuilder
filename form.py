#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 18:12:06 2019

@author: rosto
"""

from enum import Enum
import oggettoHTML

class InputType(Enum):
    PASSWORD = "password"
    TEXT = "text"
    SUBMIT = "submit"
    CHECKBOX = "checkbox"
    DATE = "date"
    EMAIL = "email"

class MethodHttp(Enum):
    POST="post"
    GET="get"
    
class Form(oggettoHTML.OggettoHTML):
    def __init__(
            self,
            ID="",
            action_url="",
            method: MethodHttp = MethodHttp.POST):
        aggiuntivi_da_passare=[]
        if action_url is not "":
            aggiuntivi_da_passare.append('action="%s"' % (action_url,))
        aggiuntivi_da_passare.append('method="%s"' % (method.value))
        super().__init__(nome_tag="form", ID=ID, classi=[""], aggiuntivi = aggiuntivi_da_passare)
    

class InputField(oggettoHTML.OggettoHTML):
    def __init__(self, ID: str,
                 label: str="",
                 inp_type: "InputType" = InputType.TEXT,
                 required: bool=False,
                 classi=[]
                 ):
        super().__init__(nome_tag="div", ID=ID, classi=classi+["input-field", "validate"])
        
        if required:
            obbligatorio: str ="required"
        else:
            obbligatorio: str = ""
        
        
        self.struttura_tag = (
            '''
            <div class="input-field col s12 m6">
              <input id="{id}" type="'''+inp_type.value+'''" class="{classi}" '''+obbligatorio+'''>
              %s
              <label for="{id}">'''+label+'''</label>
            </div>
            '''
            )

class SubmitButton(oggettoHTML.OggettoHTML):
    def __init__(self, label: str, ID: str="", classi=[]):
        super().__init__(nome_tag="button", classi=classi+["btn"], aggiuntivi=['type="submit"'])
        self.struttura_tag='<{nome_tag} id="{id}" class="{classi}" src="{src}" {aggiuntivi}>'+label+'%s</{nome_tag}>'