"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['MyApplication.py']
DATA_FILES = ["steel2.csv", "steel2mod.csv", "steel2graph.csv", "steel2corestats.csv", "steel2error.csv"]
OPTIONS = {}

setup(
    app=APP,
    data_files=DATA_FILES, 
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
