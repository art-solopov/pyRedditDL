import unittest
import tempfile
import os.path

import pyredditdl.config
from tests.processor_common_test import ProcessorCommonTest
from pyredditdl.processors import ImageProcessor

class TestImageProcessor(ProcessorCommonTest):

    def setUp(self):
        super().setUp()
        self.imgproc = ImageProcessor(self.reddit_object)

    def test_save(self):
        self.assertTrue(self.imgproc.is_processable())
        self.imgproc.process()
        self.assertTrue(os.path.exists(os.path.join(self.resdir, 'example')))
        self.assertEqual(os.listdir(os.path.join(self.resdir, 'example')), ['building.jpg'])

