import json
import yaml
import argparse
from pyredditdl.config import config, DEFAULT_CONFIG_PATH
from pyredditdl.reddit import get_link_list

def get_processors():
    return []

def main():
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', help='config path', action='store',
                        default=DEFAULT_CONFIG_PATH)
    parser.add_argument('--username', help='Reddit username',
                        action='store')
    parser.add_argument('--client_id', help='client ID', action='store')
    parser.add_argument('--secret', help='OAuth 2 secret', action='store')
    parser.add_argument('--dir', help='resulting directory', action='store')
    args = parser.parse_args()

    argvals = {k: v for k, v in vars(args).items() if v is not None}

    cfg_path = args.config
    config.update(yaml.load(open(cfg_path)))
    config.update(argvals)

    username = config['username']
    password = config['password']
    client_id = config['client_id']
    secret = config['secret']

    link_list = get_link_list(username, password, client_id, secret)
    processors = get_processors()
    for link in link_list:
        for proc in processors:
            if proc.is_processable(link):
                proc.process(link)
                break
