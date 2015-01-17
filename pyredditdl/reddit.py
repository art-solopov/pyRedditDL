import requests as req
import requests.auth as reqa
from copy import copy
import sqlite3
from datetime import date

TABLE_NAME = 'py_reddit_dl_logs'

class Reddit:

    @classmethod
    def init_log(cls, logpath):
        cls.logdb = sqlite3.connect(logpath)
        cr_cur = cls.logdb.cursor()
        cr_cur.execute("SELECT sql FROM sqlite_master"
                       "WHERE type='table' AND name=?",
                       (TABLE_NAME,))
        if len(cr_cur.fetchall()) == 0:
            cr_cur.execute("CREATE TABLE " + TABLE_NAME +
                           " (id INTEGER PRIMARY KEY, url VARCHAR(2000), date DATE")
            cls.logdb.commit()


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
        # TODO logging, retrieval with actual limit, checking for the processed links
        return response.json()['data']['children']

    def write_last_processed(self, url):
        cur = self.logdb.cursor()
        cur.execute("INSERT INTO " + TABLE_NAME + " (url, date) VALUES (?, ?)", (url, date.today()))
        self.logdb.commit()

    def get_last_processed(self):
        cur = self.logdb.cursor()
        cur.execute("SELECT url FROM " + TABLE_NAME + " ORDER BY date DESC LIMIT 1")
        return cur.fetchone()[0]


class RedditAuthError(Exception):
    pass

