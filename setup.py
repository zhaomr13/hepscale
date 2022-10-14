from distutils import sys
import os

from distutils.core import setup
from setuptools import find_packages
from setuptools.command.test import test as TestCommand

PACKAGE = "hepscale"
NAME = "hepscale"
DESCRIPTION = "An easy way to plot the scales in high energy physics"
AUTHOR = "Mingrui Zhao"
AUTHOR_EMAIL = "mingrui.zhao@mail.labz0.org"
VERSION = __import__(PACKAGE).__version__
here = os.path.dirname(__file__)
setup(
    name = NAME,
    version = VERSION,
    description = DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="Apache License, Version 2.0",
    classifiers = [
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Physics',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',

    ],
    zip_safe=False,
    keywords = "scale",
    packages = find_packages(exclude=[]),
    install_requires = [
        "matplotlib", "click"
    ],
    include_package_data = True,
    entry_points = {
        'console_scripts': [
            'hepscale = hepscale.main:main',
        ]
    }
)
