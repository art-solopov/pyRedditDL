'''Logging system for the reddit DL
used to determine the last processed link'''
import os
from pyredditdl.config import config
import json

logpath = config.get('logpath', os.path.join(os.environ['HOME'], '.pyredditdl-log'))

last_link = ''
link_count = 0

try:
    with open(logpath, 'r') as lf:
        for l in lf:
            link_count += 1
            last_link = json.loads(l)['data']['url']
except FileNotFoundError:
    print("Log file not found. Creating.")
    open(logpath, 'w')

def log(reddit_obj):
    with open(logpath, 'a') as lf:
        lf.write(json.dumps(reddit_obj) + "\n")

del lf
