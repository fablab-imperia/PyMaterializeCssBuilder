#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 17:39:47 2019

@author: rosto
"""

import oggettoHTML
from size import Size
class Column(oggettoHTML.OggettoHTML):
    def __init__(self, ID: str=""):
        super().__init__(nome_tag="div", ID=ID, classi=["col"])
    
    def add_col_size(self, num_col: int, screen_size: Size=Size.PICCOLO):
        self.add_class(Size.convert_to_class(screen_size)+str(num_col))
        