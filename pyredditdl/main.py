import json
import yaml
import argparse
from pyredditdl.config import config
from pyredditdl.reddit import get_link_list

def get_processors():
    return []

def main():
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.parse_args()

    cfg_path = config['config']
    config.update(yaml.load(open(cfg_path)))

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
