import requests as req
import requests.auth as reqa

def authentication_headers(username, password, client_id, secret, user_agent=None):
    if user_agent is None:
        user_agent = 'PyRedditDL for /u/{0}'.format(username)
    client_auth = reqa.HTTPBasicAuth(client_id, secret)
    post_data = {
        'grant_type': 'password',
        'username': username,
        'password': password
    }
    headers = {
        'User-Agent': user_agent
    }
    auth_resp = req.post('https://ssl.reddit.com/api/v1/access_token',
                         data=post_data,
                         auth=client_auth,
                         headers=headers).json()
    auth_token = '{0} {1}'.format(auth_resp['token_type'], auth_resp['access_token'])
    headers['Authorization'] = auth_token
    return headers

def get_obj_list(username, password, client_id, secret):
    headers = authentication_headers(username, password, client_id, secret)
    response = req.get('https://oauth.reddit.com/user/{0}/saved'.format(username), headers=headers)
    return response.json()['data']['children']
