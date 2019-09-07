#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 20:17:32 2019

@author: rosto
"""
import html
import oggettoHTML
class Text(oggettoHTML.OggettoHTML):
    def __init__(self,text: str, escape: bool=True):
        super().__init__()
        if escape:
            text = html.escape(text)
        self.struttura_tag = html.escape(text)
    def to_html(self) -> str:
        return self.struttura_tag
    
