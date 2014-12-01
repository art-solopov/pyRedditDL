import json
import yaml
import argparse
import requests as req
import requests.auth as reqa
import os
from os.path import join as pjoin

DEFAULT_VALUES = {
    'config': pjoin(os.environ['HOME'], 'pyredditdl.yml'),
}

def get_link_list(username, password, client_id, secret):
    client_auth = reqa.HTTPBasicAuth(client_id, secret)
    post_data = {
        'grant_type': 'password',
        'username': username,
        'password': password
    }
    headers = {
        'User-Agent': 'PyRedditDL for /u/{0}'.format(username)
    }
    auth_resp = req.post('https://ssl.reddit.com/api/v1/access_token',
                         data=post_data,
                         auth=client_auth,
                         headers=headers).json()
    auth_token = '{0} {1}'.format(auth_resp['token_type'], auth_resp['access_token'])
    headers['Authorization'] = auth_token
    response = req.get('https://oauth.reddit.com/user/{0}/saved'.format(username), headers=headers)
    return response.json()

def get_processors():
    pass

def main():
    # Parse arguments
    username = ''
    password = ''
    link_list = get_link_list(username, password)
    processors = get_processors()
    for link in link_list:
        for proc in processors:
            if proc.is_processable(link):
                proc.process(link)
                break
