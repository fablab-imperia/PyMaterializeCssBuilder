#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 17:36:22 2019

@author: rosto
"""

import oggettoHTML
class Container(oggettoHTML.OggettoHTML):
    def __init__(self,ID=""):
        super().__init__(nome_tag="div", ID=ID, classi=["container"])
