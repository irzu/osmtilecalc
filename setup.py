#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup script for osmtilecalc.
https://github.com/irzu/osmtilecalc
"""
import os
from setuptools import setup, find_packages

setup(
    name="osmtilecalc",
    version="0.1.1",
    description="Calculates Open Street Map tile coordinates.",
    long_description=open(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md")
    ).read(),
    long_description_content_type="text/markdown",
    author="Irek Żuchowski",
    author_email="irek@atarnia.com",
    url="https://github.com/irzu/osmtilecalc",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["setuptools"],
    setup_requires=["pytest-runner"],
    entry_points={"console_scripts": ["osmtilecalc = osmtilecalc.main:main"]},
)
