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
        'praw>=2.1.19',
        'PyYAML>=3.11',
    ],

    entry_points={
        'console_scripts': [
            'py_reddit_dl = pyredditdl.main.main'
        ]
    }
)
