import json
import yaml
import requests

class RedditTalker:
    def __init__(self, config):
        with open(config, 'r') as cfg_file:
            self.config = yaml.load(cfg_file.read())

def main():
    print("Hello world!")
