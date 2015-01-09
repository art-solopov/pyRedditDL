import unittest
import tempfile
import os.path

import pyredditdl.config

class ProcessorCommonTest(unittest.TestCase):
    def setUp(self):
        self.reddit_object = {
            'kind': 't3',
            'data': {
                'subreddit': 'example',
                'title': "Example Subreddit object",
                'url': 'http://loremflickr.com/320/240/building.jpg',
            }
        }

        self.resdir = tempfile.mkdtemp('pyredditdl-test')
        pyredditdl.config.config['dir'] = self.resdir
