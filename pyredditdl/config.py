import os
from os.path import join as pjoin
HOME = os.environ['HOME']

DEFAULT_VALUES = {
    'config': pjoin(HOME, 'pyredditdl.yml'),
    'dir': pjoin(HOME, 'Reddit'),
}

config = DEFAULT_VALUES
