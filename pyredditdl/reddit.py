import requests as req
import requests.auth as reqa
from copy import copy

class Reddit:
    def __init__(self, username, password, client_id, secret):
        self.username = username
        self.password = password
        self.client_id = client_id
        self.secret = secret
        self.headers = {
            'User-Agent': 'PyRedditDL for /u/{0}'.format(self.username)
        }

    def authenticate(self):
        client_auth = reqa.HTTPBasicAuth(self.client_id, self.secret)
        headers = copy(self.headers)
        post_data = {
            'grant_type': 'password',
            'username': self.username,
            'password': self.password
        }
        auth_resp = req.post('https://ssl.reddit.com/api/v1/access_token',
                             data=post_data,
                             auth=client_auth,
                             headers=headers)
        if auth_resp.status_code >= 400:
            raise RedditAuthError()
        auth_resp_body = auth_resp.json()
        auth_token = '{0} {1}'.format(auth_resp_body['token_type'], auth_resp_body['access_token'])
        self.headers['Authorization'] = auth_token

    def get_obj_list(self, limit=1000):
        response = req.get('https://oauth.reddit.com/user/{0}/saved'.format(self.username), headers=self.headers)
        # TODO logging, retrieval with actual limit
        return response.json()['data']['children']

class RedditAuthError(Exception):
    pass

