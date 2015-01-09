import unittest
import tempfile
import os.path

import pyredditdl.config
from tests.processor_common_test import ProcessorCommonTest
from pyredditdl.processors import LogProcessor

class TestLogProcessor(ProcessorCommonTest):

    def setUp(self):
        super().setUp()
        self.logproc = LogProcessor(self.reddit_object)



    def test_log(self):
        self.assertTrue(self.logproc.is_processable())
        self.logproc.process()
        logpath = os.path.join(self.resdir, 'example', '__not_saved.log')
        self.assertTrue(os.path.exists(logpath))
        with open(logpath) as logf:
            self.assertEqual(list(logf), [self.logproc.url + "\n"])
