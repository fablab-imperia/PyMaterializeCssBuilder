#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 20:35:38 2019

@author: rosto
"""
import text
import oggettoHTML
class Link(oggettoHTML.OggettoHTML):
    def __init__(self, text_displayed: str, url: str, ID=""):
        super().__init__(nome_tag="a", ID=ID, aggiuntivi=['href="'+url+'"'])
        self.add_child(text.Text(text_displayed))
        