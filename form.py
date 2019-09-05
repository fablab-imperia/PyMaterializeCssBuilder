#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 18:12:06 2019

@author: rosto
"""

from enum import Enum
import oggettoHTML
class Form(oggettoHTML.OggettoHTML):
    def __init__(self,ID=""):
        super().__init__(nome_tag="div", ID=ID, classi=["row"])
    

class InputField(oggettoHTML.OggettoHTML):
    def __init__(self,
                 ID="",
                 label: str,
                 inp_type: InputType = InputType.TEXT,
                 required: bool=False,
                 ):
        super().__init__(nome_tag="div", ID=ID)
        
        if required:
            obbligatorio: str ="required"
        else:
            obbligatorio: str = ""
        
        self.struttura_tag = (
            f"""
            <div class="input-field col s12 m6">
              <input id="{id}" type=" """+inp_type.value+""" " class="{classi}" """+obbligatorio+""">
              <label for="{id}">"""+label+"""</label>
            </div>
            """
            )

class InputType(Enum):
    PASSWORD = "password"
    TEXT = "text"
    SUBMIT = "submit"
    CHECKBOX = "checkbox"