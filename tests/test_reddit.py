import unittest
import mock
import json
import hashlib

from pyredditdl.reddit import Reddit, req, reqa

class TestReddit(unittest.TestCase):
    def setUp(self):
        hl = hashlib.md5()
        hl.update(b'Access token')
        self.access_token = hl.hexdigest()

        self.reqa_auth_mock = mock.MagicMock(name='reqa.HTTPBasicAuth')
        self.reqa_auth_mock.return_value = mock.MagicMock()

        self.req_post_mock = mock.MagicMock(name='req.post')
        self.req_post_mock.return_value.status_code = 200
        self.req_post_mock.return_value.json.return_value = {
            'token_type': 'bearer',
            'access_token': self.access_token
        }

        self.req_get_mock = mock.MagicMock(name='req.get')
        self.req_get_mock.return_value.json.return_value = json.load(open('tests/fixture/test.json'))

        reqa.HTTPBasicAuth = self.reqa_auth_mock
        req.post = self.req_post_mock
        req.get = self.req_get_mock

    def test_authentication(self):

        reddit = Reddit('testuser', 'testpwd', 'testcli', 'testsecret')

        headers = {
            'User-Agent': 'PyRedditDL for /u/testuser',
            'Authorization': 'bearer ' + self.access_token
        }

        reddit.authenticate()

        self.assertEqual(reddit.headers, headers)
        self.reqa_auth_mock.assert_called_once_with('testcli', 'testsecret')
        self.req_post_mock.assert_called_once_with(
            'https://ssl.reddit.com/api/v1/access_token',
            data=dict(grant_type='password',
                      username='testuser',
                      password='testpwd'),
            auth=self.reqa_auth_mock(),
            headers={'User-Agent': 'PyRedditDL for /u/testuser'})
