#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 20:33:25 2019

@author: rosto
"""
import link
from typing import List
import oggettoHTML
class Navbar(oggettoHTML.OggettoHTML):
    def __init__(self, list_links: List[link.Link] = [], ID="", classi: List[str] = []):
        super().__init__(ID=ID, classi=classi+["left", "hide-on-med-and-down"])
        
        self.struttura_tag = (
                """
                <nav>
                  <div class="nav-wrapper">
                    <ul id="{id}" class="{classi}"">
                      %s
                    </ul>
                  </div>
                </nav>
                """
                )
        
        
  
        