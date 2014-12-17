import unittest
import tempfile
import os.path

import pyredditdl.config
from pyredditdl.processors import ImageProcessor

class TestImageProcessor(unittest.TestCase):

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

        self.imgproc = ImageProcessor(self.reddit_object)

        self.resdir = tempfile.mkdtemp('pyredditdl-test')

        pyredditdl.config.config['dir'] = self.resdir

    def test_save(self):
        self.assertTrue(self.imgproc.is_processable())
        self.imgproc.process()
        self.assertTrue(os.path.exists(os.path.join(self.resdir, 'example')))
        self.assertEqual(os.listdir(os.path.join(self.resdir, 'example')), ['building.jpg'])

