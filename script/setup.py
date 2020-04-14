#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
from Cython.Build import cythonize


setup(
    name = "Hello world app",
    ext_modules = cythonize("mytest.py"),
)

