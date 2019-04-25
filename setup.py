#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: eaglewings
# E-Mail: ZWFnbGV3aW5ncy55aUBnbWFpbC5jb20=
# Created  Time: 2019-04-24 19:21
# Last Modified:
# Description:
#        - Project:   BT Trackers Updater
#        - File Name: setup.py
#        - setup file

"""
  ______                __                __  __          __      __
 /_  __/________ ______/ /_____  _____   / / / /___  ____/ /___ _/ /____  _____
  / / / ___/ __ `/ ___/ //_/ _ \/ ___/  / / / / __ \/ __  / __ `/ __/ _ \/ ___/
 / / / /  / /_/ / /__/ ,< /  __/ /     / /_/ / /_/ / /_/ / /_/ / /_/  __/ /
/_/ /_/   \__,_/\___/_/|_|\___/_/      \____/ .___/\__,_/\__,_/\__/\___/_/
                                           /_/
"""


import setuptools

with open("README.md", "r") as file:
    long-description = file.read()

setuptools.setup(
    name="BT-Tracker",
    version="0.2.3",
    author="eaglewings",
    author_email="eaglewings.yi@gmail.com",
    description="A command line interface BT Trackers Updater.",
    long_description=long-description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=setuptools.find_packages(),
    keywords=["aria2", "Tracker", "cli", "updater"],
    include_package_data=True,
    entry_points={"console_scripts": ["BT-Tracker = Tracker.main:start"]},
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
