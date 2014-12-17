'''
Setuptools data
'''
from setuptools import setup, find_packages

setup(
    name="pyRedditDL",
    version='0.1',
    packages=find_packages(),

    author="Artemiy Solopov",
    author_email="art-solopov@yandex.ru",
    description="Program for automatic download of Reddit saved links",
    license="GNU GPL v3",

    install_requires=[
        'PyYAML>=3.11',
        'requests>=2.4.3',
        'Pillow>=2.6',
    ],

    tests_require=[
        'nose>=1.3',
    ],

    test_suite='nose.collector',

    entry_points={
        'console_scripts': [
            'py_reddit_dl = pyredditdl.main:main'
        ],
        'reddit_link_processors':
            [
                'image = pyredditdl.processors:ImageProcessor',
                'log = pyredditdl.processors:LogProcessor'
            ]
    }
)
