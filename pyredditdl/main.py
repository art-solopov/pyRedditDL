import json
import yaml
import argparse
import requests

def get_link_list(username, password):
    pass

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
