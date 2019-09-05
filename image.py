#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 18:01:38 2019

@author: rosto
"""

import oggettoHTML
class Image(oggettoHTML.OggettoHTML):
    def __init__(self, src: str, ID=""):
        super().__init__(nome_tag="img", ID=ID, classi=["responsive-img"], src=src)
    
    def set_circular_image(self, state: bool) -> None:
        if state:
            self.add_class("circle")
        else:
            self.remove_class("circle")