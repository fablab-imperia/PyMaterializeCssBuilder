#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 17:47:21 2019

@author: rosto
"""
from enum import Enum

class Size(Enum):
        PICCOLO=1
        MEDIO=2
        GRANDE=3
        MOLTO_GRANDE=4
        
        def convert_to_class(size) -> str:
            a = {
                    Size.PICCOLO:"s",
                    Size.MEDIO: "m",
                    Size.GRANDE: "l",
                    Size.MOLTO_GRANDE: "xl"
                }
            return a.get(size,"s")