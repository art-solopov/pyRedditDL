# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 00:06:47 2014

@author: art-solopov
"""
import mimetypes
from requests import get
from PIL import Image
from tempfile import mkstemp
from os import fdopen
from pyredditdl.config import config
import os.path

class BaseProcessor:
    '''The higher the priority value, the higher will the plugin stand in the
    responsibility queue'''
    priority = 0

    def __init__(self, reddit_obj):
        self.reddit_obj = reddit_obj
        self.url = reddit_obj['data']['url']
        self.subreddit = reddit_obj['data']['subreddit']

    def is_processable(self):
        '''This function determines whether this processor is suitable for processing
        this particular Reddit object'''
        return False

    def process(self):
        '''This function is used to process the Reddit object'''
        raise NotImplementedError

class ImageProcessor(BaseProcessor):
    '''Saves the image files'''

    priority = 1

    def is_processable(self):
        mime_type = mimetypes.guess_type(self.url)[0]
        return (mime_type is not None) and (mime_type.startswith('image'))

    def process(self):
        response = get(self.url)
        tmpfd, tmpfname = mkstemp(prefix='tmp_pyredditdl_')
        with fdopen(tmpfd, 'wb') as tmpf:
            tmpf.write(response.content)
        img = Image.open(tmpfname)
        filename = os.path.basename(self.url)
        path = os.path.join(config['dir'], self.subreddit)
        if not os.path.exists(path):
            os.mkdir(path)
        img.save(os.path.join(path, filename))

class LogProcessor(BaseProcessor):
    '''Logs the urls. Should always be the last one in the queue'''

    def is_processable(self):
        return True

    def process(self):
        fname = os.path.join(config['dir'], self.subreddit, '__not_saved.log')
        with open(fname, 'a') as logf:
            logf.write(self.url + "\n")
