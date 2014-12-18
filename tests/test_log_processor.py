import unittest
import tempfile
import os.path

import pyredditdl.config
from pyredditdl.processors import LogProcessor

class TestLogProcessor(unittest.TestCase):

    def setUp(self):
        self.reddit_object = {
            'kind': 't3',
            'data': {
                'subreddit': 'example',
                'title': "Example Subreddit object",
                'url': 'http://loremflickr.com/320/240/building.jpg',
                # TODO move the example in a separate object
                # TODO fill more fields
            }
        }

        self.resdir = tempfile.mkdtemp('pyredditdl-test')
        pyredditdl.config.config['dir'] = self.resdir

        self.logproc = LogProcessor(self.reddit_object)



    def test_log(self):
        self.assertTrue(self.logproc.is_processable())
        self.logproc.process()
        logpath = os.path.join(self.resdir, 'example', '__not_saved.log')
        self.assertTrue(os.path.exists(logpath))
        with open(logpath) as logf:
            self.assertEqual(list(logf), [self.logproc.url + "\n"])
