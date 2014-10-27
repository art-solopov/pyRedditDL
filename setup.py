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
    license="GNU GPL v3"
)
