# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 00:06:47 2014

@author: art-solopov
"""
import mimetypes

class ImageProcessor:
    
    def __init__(self, path):
        self.path = path
        
    def is_processable(self):
        tp = mimetypes.guess_type(self.path)[0]
        return (tp is not None) and (tp.startswith('image'))
    
    def process(self):
        pass #TODO write later