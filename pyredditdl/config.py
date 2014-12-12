import os
from os.path import join as pjoin
HOME = os.environ['HOME']

DEFAULT_CONFIG_PATH = pjoin(HOME, 'pyredditdl.yml')

DEFAULT_VALUES = {
    'dir': pjoin(HOME, 'Reddit'),
}

config = DEFAULT_VALUES
