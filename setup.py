import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Brahma",
    version = "1.0",
    author = "Devansh Raghav",
    author_email = "indiananonymous75@gmail.com",
    description = ("A tool that automates other tools"),
    license = "MIT",
    keywords = ["Brahma", "Bug Bounty", "pentesting", "security", "hacking"],
    url = "https://github.com/DevanshRaghav75/Brahma",
    packages=find_packages(),
    long_description=read('README.md'),
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],
    package_data={'Brahma': ['db/*']},
    install_requires=[
        'colorama',
    ],

    entry_points={
        'console_scripts': [
            'Brahma = Brahma.__main__:main'
        ]
    },
)
