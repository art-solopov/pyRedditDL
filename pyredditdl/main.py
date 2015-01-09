import json
import yaml
import argparse
from pyredditdl.config import config, DEFAULT_CONFIG_PATH
from pyredditdl.reddit import Reddit
from pyredditdl.logging import last_link, init_log, log
import pkg_resources

def get_processors():
    procs = [e.load() for e in pkg_resources.iter_entry_points('reddit_link_processors')]
    procs.sort(key=lambda x: x.priority, reverse=True)
    return procs

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

    reddit = Reddit(username, password, client_id, secret)
    reddit.authenticate()
    obj_list = reddit.get_obj_list()

    processors = get_processors()
    init_log()
    for obj in obj_list:
        if obj['data']['url'] == last_link:
            break
        for pr_cls in processors:
            proc = pr_cls(obj)
            if proc.is_processable():
                proc.process()
                break
        log(obj)
